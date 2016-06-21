from geopy.geocoders import Nominatim

gmaps = Nominatim()
address = gmaps.geocode("175 5th Avenue NYC")
print (address.address)
print ((address.latitude, address.longitude))
