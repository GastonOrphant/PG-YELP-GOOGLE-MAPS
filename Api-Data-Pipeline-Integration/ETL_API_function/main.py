import pandas as pd
from textblob import TextBlob
import datetime
from google.cloud import bigquery
from pandas.io import gbq
import re
import os
from google.cloud import storage
import json
import requests
from urllib.request import Request


# function to send a message in the slack 
def enviar_mensaje_slack(request):
    webhook_url = 'https://hooks.slack.com/services/custom-link-in-slack-api'
    mensaje = 'Los datos de las apis se han cargado con éxito'
    headers = {'Content-type': 'application/json'}
    payload = {'text': mensaje}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    print('Mensaje enviado:', response.status_code, response.text)
    return 'Mensaje enviado'

#  Function to classify comments
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


def procesar_datos_json(event, context, request):
    # Open the JSON file and load it into a DataFrame
    file_name = event['name']
    print(file_name)
    df = pd.read_json(f"gs://{event['bucket']}/{file_name}")
    
    # Rename the column 'rating' to 'rating_avg'.
    df= df.rename(columns={'rating':'rating_avg'})
    print(df.head(2))
    
    # Drops columns that have no rating 
    df = df.drop(df.loc[df['rating_avg'] == 'N/A'].index)
    
    # Adds column depending on the state
    filename = os.path.splitext(os.path.basename(event['name']))[0]
    print(filename)
    
    # Maps the file name to a state
    state_mapping = {
        'California': 'CA',
        'Texas': 'TX',
        'Pensilvania': 'PA',
        'Florida': 'FL',
        'NuevaYork': 'NY'
    }

     # Add "state" column to DataFrame
    df['state'] = state_mapping.get(filename)
    
    # Unnest the 'reviews' column
    df_expanded = df.explode('reviews').reset_index(drop=True)

    # Filter out only the items in the 'reviews' column that are dictionaries
    df_expanded = df_expanded[df_expanded['reviews'].apply(lambda x: isinstance(x, dict))]

    # Normalize the 'reviews' column
    reviews_df = pd.json_normalize(df_expanded['reviews'])
    reviews_df = reviews_df.add_prefix('reviews.')

    # Join the original DataFrame with the normalized reviews DataFrame.
    df_data = pd.concat([df_expanded.drop('reviews', axis=1), reviews_df], axis=1)

    # Extract the user_id from the reviews.author_url column.
    new=df_data['reviews.author_url'].str.split(pat='/', n=6,expand=True)
    df_data['user_id']=new[5]
    df_data['user_id'] = df_data['user_id'].astype(str)

    # Add a sentiment column 
    df_data['feeling'] = df_data['reviews.text'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')
    
    # Add the columns to have the same format as the other platform data.
    df_data['main_category']='food services'
    df_data['num_of_reviews']= 0
    df_data['platform']='detailsApi'
    df_data['resp']= "No response"

    # Rename some columns
    df_data = df_data.rename(columns={'reviews.rating': 'rating','reviews.time':'date','reviews.text': 'opinion', 'place_id':'business_id','name':'local_name'})
    df_data = df_data[['user_id','business_id','local_name','latitude','longitude','num_of_reviews','state','main_category','date','rating','resp','opinion','feeling','platform']]
   
    # Removes emojis and strange characters from the opinion column 
    df_data['opinion'] = df_data['opinion'].str.replace('"', '')
    df_data['opinion'] = df_data['opinion'].apply(lambda x: x.encode('unicode-escape').decode('utf-8'))
    
    # Removes duplicates
    df_data.drop_duplicates(inplace=True)

    # Send data to the data warehouse in csv format
    df_data.to_csv('gs://' + 'datasets-pg' + '/' + 'Details-Api' + '/' + filename + '.csv',index=False)
    
    # Send completion message to slack group 
    enviar_mensaje_slack()

    return 'done'
