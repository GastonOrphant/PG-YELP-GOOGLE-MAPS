import os
import requests
from flask import jsonify
from google.cloud import storage
import json
import random 
import pandas as pd

# a random function is added to change a little the longitude and latitude to obtain different results
def get_random_offset():
    return random.uniform(-0.01, 0.01)

def search_restaurants(request):
    locations = {
        "California": ["San Mateo","San Francisco", "Los Angeles", "San Diego", "Sacramento", "Santa Clara", "Fresno","Alameda", "Orange","Kern","Riverside", "San Joaquin","Contra Costa","Ventura"],
        "Texas": ["Harris","Dallas","Tarrant","Bexar","Travis","Collin","Denton","Hidalgo"," El Paso","Fort Bend","Montgomery","Williamson","Cameron","Nueces"],
        "Florida":["Miami-Dade","Broward","Palm Beach","Hillsborough","Orange","Pinellas","Duval","Lee","Polk","Brevard","Volusia","Pasco","Seminole","Sarasota"],
        "NuevaYork":["Kings","Queens","New York","Bronx","Richmond","Suffolk","Nassau","Westchester","Erie","Monroe","Onondaga","Orange","Rockland","Albany"],
        "Pensilvania":["Philadelphia","Allegheny","Delaware","Montgomery","Bucks","Lehigh","Lancaster","Chester","Northampton","Dauphin","Erie","Luzerne","York","Westmoreland"]
    }
    api_key = API_KEY
    
    for state, cities in locations.items():
        random.shuffle(cities)  #  rearrange the cities
        restaurant_data = []
        for city in cities:
            # the city coordinates are obtained
            geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city},{state}&key={api_key}'
            geocoding_response = requests.get(geocoding_url)
            geocoding_result = geocoding_response.json()['results'][0]
            location_lat = geocoding_result['geometry']['location']['lat']+ get_random_offset()
            location_lng = geocoding_result['geometry']['location']['lng']+ get_random_offset()

            # search parameters
            query = 'restaurant'
            radius = 50000
            fields = 'name,rating,formatted_address,geometry,reviews'

            # we search with the coordinates for restaurants within 50km 
            url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location_lat},{location_lng}&radius={radius}&type={query}&key={api_key}'

            # we make the request and get the results
            response = requests.get(url)
            results = response.json()['results']

            # for each result you get the details you need
            for result in results:
                place_id = result['place_id']
                details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields={fields}&key={api_key}'
                details_response = requests.get(details_url)
                details = details_response.json()['result']

                # Obtaining the required data and adding them to the dictionary
                restaurant = {
                    'name': details['name'],
                    'rating': details.get('rating', 'N/A'),
                    'address': details['formatted_address'],
                    'latitude': details['geometry']['location']['lat'],
                    'longitude': details['geometry']['location']['lng'],
                    'reviews': details.get('reviews', []),
                    'place_id': place_id
                }
                restaurant_data.append(restaurant)

        # json is flattened 
        df = pd.json_normalize(restaurant_data)

        # from data we converted it to a dictionary
        restaurant_data_flat = df.to_dict('records') 

        # Saving JSON file
        storage_client = storage.Client()
        bucket_name = 'extra_sources'
        file_name = f"{state}.json"
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"Details-Api/{file_name}")
        blob.upload_from_string(json.dumps(restaurant_data_flat, indent=1, separators=(',', ': ')))

    return 'Done'
