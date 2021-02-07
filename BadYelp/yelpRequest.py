import yelpAPI
import requests
import json

yelpAPI_key = yelpAPI.get_key()
BUSINESS_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
BUSINESS_INFO_ENDPOINT = 'https://api.yelp.com/v3/businesses/'
HEADERS = {'Authorization' : "Bearer " + yelpAPI_key}
DEFAULT_TERM = 'food'
DEFAULT_LOCATION = 'Los Angeles, CA'

def getSearchParams(term, location):
    term.strip()
    params = {}
    if term: 
        params['term'] = term
    else:#no term provided
        params['term'] = DEFAULT_TERM
    
    if location:
        params['location'] = location
    else:
        params['location'] = DEFAULT_LOCATION
    
    params['radius'] = 10000
    params['limit'] = 5
    #params['sort_by'] = 'rating'

    return params

def searchBusinesses(term, location):
    response = requests.get(url = BUSINESS_SEARCH_ENDPOINT, params= getSearchParams(term, location), headers = HEADERS)
    dictResp = response.json()
    dictRespClean = dictResp["businesses"]
    #sort by lowest rating
    dictRespClean.sort(key=lambda biz: biz['rating'])

    return dictRespClean

def getBusinessInfo(bizID):
    response = requests.get(url = BUSINESS_INFO_ENDPOINT + bizID, headers = HEADERS)
    return response.json()
