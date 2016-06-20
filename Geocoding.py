from googlemaps import GoogleMaps

gmaps = GoogleMaps(AIzaSyDK9zd0m8qvDcS-Nl9SxUflRk9nRFi-EuM)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng
