import yelpAPI
import requests
import json
yelpAPI_key = yelpAPI.get_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization' : "Bearer " + yelpAPI_key}

#params
PARAMETERS = {'term': 'coffee',
              'limit': 2,
              'radius': 1000,
              'location': 'San Diego'}

#make request from yelp api
response = requests.get(url = ENDPOINT, params= PARAMETERS, headers = HEADERS)

print(response.json())