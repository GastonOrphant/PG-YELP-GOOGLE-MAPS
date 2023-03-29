import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery
from textblob import TextBlob
import re
import functions_framework

'''
Python Dependencies to be installed

gcsfs
fsspec
pandas
pandas-gbq

'''

# We define the main_categories
food_services = ["restaurant","cafe"]
hotel_services = ["hotel","hostel"]
health_care_services = ["medical","dental","dentist","hospital"]


def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    lst = []
    # Extract the name of the event, included the name of all the carpets
    file_name = event['name']
    # Extract the type of the file
    file_type = file_name.split('.')[-1]
    # Extract the name of the file
    if "/" in file_name:
        main_folder = file_name.split("/")[0]
        last_folder = file_name.split("/")[file_name.count("/")-1]
        if main_folder == "Google-Maps":
            if file_name.split("/")[1] == "reviews-estados":
                table_name = "Reviews"
                state = last_folder.split("-")[-1]
                dataset = main_folder.split("-")[0] + "."
            if file_name.split("/")[1] == "metadata-sitios":
                table_name = "Metadata"
                dataset = main_folder.split("-")[0] + "."
        if main_folder == "Yelp":
            table_name = file_name.split(".")[0].split("/")[1]
            dataset = "yelp."
            if "review" in table_name:
                table_name = "review"
        if main_folder == "Details-Api":
            table_name = file_name.split(".")[0].split("/")[1]
            dataset = "new_sources."
    else:
        table_name = file_name.split('.')[0]
        dataset = "new_sources."

    # Event,File metadata details writing into Big Query
    dct={
         'Event_ID':context.event_id,
         'Event_type':context.event_type,
         'Bucket_name':event['bucket'],
         'File_name':event['name'],
         'Created':event['timeCreated'],
         'Updated':event['updated']
        }
    lst.append(dct)
    df_metadata = pd.DataFrame.from_records(lst)
    df_metadata.to_gbq(dataset + 'data_loading_metadata', 
                        project_id='concrete-bridge-379920', 
                        if_exists='append',
                        location='us')
    
    # Check if the type of the file is csv
    if file_type == "csv":
        # Actual file data , writing to Big Query
        df_data = pd.read_csv('gs://' + event['bucket'] + '/' + file_name)

    # Check if the type of the file is json    
    if file_type == "json":
        # Actual file data , writing to Big Query
        try:
            # Load the Json file
            df_data = pd.read_json('gs://' + event['bucket'] + '/' + file_name)
        except ValueError as e:
            if "Trailing data" in str(e):
                # Execute this alternative line of code
                df_data = pd.read_json('gs://' + event['bucket'] + '/' + file_name, lines = True)
            else:
                # Manage other kind of errors
                print("An error occurred while loading the JSON file:", e)
        
    # Check if the type of the file is parquet
    if file_type == "parquet":
        # Actual file data , writing to Big Query
        df_data = pd.read_parquet('gs://' + event['bucket'] + '/' + file_name)
    
    # -= Transformations Part =-
    # Google Transformations
    # Transformations if We are uploading data related to reviews divided by USA States.
    if main_folder == "Google-Maps":
        if last_folder == "reviews-estados":
            df_data['user_id'] = df_data['user_id'].astype(str)
            df_data.drop(columns=["name","pics"],inplace=True)
            df_data.rename(columns={"text":"opinion", "time":"date","gmap_id":"business_id"}, inplace=True)
            df_data["date"] = pd.to_datetime(df_data['date'], unit='ms').dt.strftime('%Y-%m-%d')
            df_data['date'] = pd.to_datetime(df_data['date'], format='%Y-%m-%d')
            df_data['feeling'] = df_data['opinion'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')
            
            if state == "California":
                df_data["state"] = "CA"
            if state == "New_York":
                df_data["state"] = "NY"
            if state == "Pennsylvania":
                df_data["state"] = "PA"
            if state == "Texas":
                df_data["state"] = "TX"
            if state == "Florida":
                df_data["state"] = "FL"

        # Transformations if We are uploading data related to USA Stores.
        if last_folder == "metadata-sitios":
            df_data["platform"] = "google"
            df_data.drop(columns=["description","price","MISC","hours","state","relative_results","address","url"],axis = 1,inplace=True)
            df_data.rename(columns={"name":"local_name","gmap_id":"business_id"}, inplace=True)
            df_data['category'] = df_data['category'].apply(lambda x: clear_categories(x) if pd.notnull(x) else 'No category assigned')
            df_data["category"] = df_data["category"].str.lower()
            df_data["main_category"] = "other"
            df_data["main_category"] = df_data.apply(categorize, axis=1)
            df_data.drop_duplicates(inplace=True)

    #--------------- Yelp Transformations -----------
    if main_folder == "Yelp":
        if  table_name == "review":
            df_data.drop(columns=["cool","funny","useful"], inplace=True)
            df_data.rename(columns={"text":"opinion", "stars":"rating"}, inplace=True)
            df_data['date'] = pd.to_datetime(df_data['date']).dt.strftime('%Y-%m-%d')
            df_data['date'] = pd.to_datetime(df_data['date'], format='%Y-%m-%d')
            df_data['feeling'] = df_data['opinion'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')
    
        if table_name == "business":
            states = ["TX", "CA", "PA", "NY", "FL"]
            df_data["platform"] = "yelp"
            df_data = df_data[df_data["state"].isin(states)]
            df_data.drop(columns=["address","postal_code","is_open","attributes","hours"], inplace=True)
            df_data.rename(columns={"name":"local_name", "review_count":"num_of_reviews","categories":"category"}, inplace=True)
            df_data['category'] = df_data['category'].apply(lambda x: clear_categories(x) if pd.notnull(x) else 'No category assigned')
            df_data["category"] = df_data["category"].str.lower()
            df_data["main_category"] = "other"
            df_data["main_category"] = df_data.apply(categorize, axis=1)
            df_data.drop_duplicates(inplace=True)

        if table_name == "user":
            df_data.drop(columns=["Unnamed: 0","name","yelping_since","funny","cool","elite","fans","average_stars","compliment_hot","compliment_more","compliment_profile","compliment_cute","compliment_list","compliment_note","compliment_plain","compliment_cool","compliment_funny","compliment_writer","compliment_photos"],inplace=True)
            df_data.rename(columns={"review_count":"num_of_reviews"}, inplace=True)
        
        if table_name == "tip":
            df_data.rename(columns={"text":"opinion"}, inplace=True)
            df_data['feeling'] = df_data['opinion'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')
        
        df_data.drop_duplicates(inplace=True)

    if main_folder == "Details-Api":
 
        df_data["date"] = pd.to_datetime(df_data['date'], unit='s').dt.strftime('%Y-%m-%d')
        df_data['date'] = pd.to_datetime(df_data['date'], format='%Y-%m-%d')
        
        table_name = "new_data"
        df_data.to_gbq(dataset + table_name, 
                            project_id='concrete-bridge-379920', 
                            if_exists='append',
                            location='us')   
    else:
        df_data.to_gbq(dataset + table_name, 
                            project_id='concrete-bridge-379920', 
                            if_exists='append',
                            location='us')

# Function to classify comments
def classify_comment2(comment):
    if comment is None:
        return 'No message'
    else:
        sentiment = TextBlob(comment).sentiment.polarity
        if sentiment > 0:
            return 'Positive'
        elif sentiment < 0:
            return 'Negative'
        else:
            return 'Neutral'

# Define a function to apply to each register in the "category" column
def clear_categories(chain):
    # Remove brackets, single and double quotes.
    clean_chain = re.sub(r"[\[\]'\"]", '', chain)
    if chain in ",":
        # Separate words by comas and return them.
        return clean_chain.split(',')
    else:
        return clean_chain
    
# Function to categorize businesses and store them in a new colum called "category".
def categorize(row):

    if any(keyword in row["category"] for keyword in hotel_services):
        return "hotel services"

    elif any(keyword in row["category"] for keyword in food_services):
        return "food services"
    
    elif any(keyword in row["category"] for keyword in health_care_services):
        return "health care services"
    
    elif row["category"] == "No category assigned":
        return "No category assigned"

    else:
        return "other"