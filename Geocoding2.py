from googlemaps import Client as GoogleMaps
from googlemaps.geocoding import geocode

API_Key="AIzaSyDVYcV4L2bOFuiEvjgvtTWsVieX7nZfzeo"

gmaps = GoogleMaps(API_Key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng
print lat, lng
