from googlemaps import Client as GoogleMaps
from googlemaps import geocoding
from googlemaps import convert

API_Key="AIzaSyDVYcV4L2bOFuiEvjgvtTWsVieX7nZfzeo"

gmaps = GoogleMaps(API_Key)
address = raw_input("Enter a location: ")
coordinates = gmaps.geocode(address)
print coordinates
