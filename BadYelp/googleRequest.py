import googlemaps
import googleAPI

API_key = googleAPI.get_key()   #enter the key you got from Google. I removed mine here

gmaps = googlemaps.Client(key=API_key)
 
def getMinutes(origin, destination):
    result = gmaps.distance_matrix(origin, destination, mode='walking')["rows"][0]["elements"][0]["duration"]["text"]  
    return result
