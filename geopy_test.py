'''from geopy.geocoders import Nominatim   
geolocator = Nominatim()
location = geolocator.geocode("CARD MOTTA")
print(location.address)

print((location.latitude, location.longitude))
print(location.raw)
''' 

from geopy.geocoders import GoogleV3

point = '51.523910, -0.158578' #here's famous Sherlock Holmes' museum lat & lng

geolocator = GoogleV3()
#address = geolocator.reverse(point)
address = geolocator.geocode("Alameda Tiete")
print(address[0]) # use other indexes if you want more or less detailed address scope.
print(address.raw)