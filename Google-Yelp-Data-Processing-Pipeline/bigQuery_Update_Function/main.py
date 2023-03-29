from google.cloud import bigquery

# This Function will update our main table "platform_reviews" (Data Warehouse) with new data, excluding duplicates
def hello_world(request):
    client = bigquery.Client()
    query = """
        INSERT INTO Google.platform_reviews (user_id, business_id, local_name, latitude, longitude, num_of_reviews , state, main_category, date, rating, resp, opinion, feeling, platform)
        SELECT user_id, business_id, local_name, latitude, longitude, num_of_reviews , state, main_category, date, rating, resp, opinion, feeling, platform FROM new_sources.new_data WHERE NOT EXISTS (SELECT 1 FROM Google.platform_reviews WHERE platform_reviews.user_id = new_data.user_id AND platform_reviews.business_id = new_data.business_id AND platform_reviews.local_name = new_data.local_name AND platform_reviews.latitude = new_data.latitude AND platform_reviews.longitude = new_data.longitude AND platform_reviews.num_of_reviews = new_data.num_of_reviews AND platform_reviews.state = new_data.state AND platform_reviews.main_category = new_data.main_category AND platform_reviews.date = new_data.date AND platform_reviews.rating = new_data.rating AND platform_reviews.resp = new_data.resp AND platform_reviews.opinion = new_data.opinion AND platform_reviews.feeling = new_data.feeling)
    """
    query_job = client.query(query)
    query_job.result()

    return "Update Done"
    
