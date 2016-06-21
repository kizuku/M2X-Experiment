#Python Get Directions Script

#API_KEY value
API_KEY="AIzaSyDVYcV4L2bOFuiEvjgvtTWsVieX7nZfzeo"

#import statements
from googlemaps import Client

#create GoogleMaps object
mapService = Client(API_KEY)

#get directions from google
directions = mapService.directions('texarkana', 'atlanta')
for key in  directions:
    print(key)
