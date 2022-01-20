from geopy.geocoders import Nominatim


#Parque Nacional da Tijuca - Alto da Boa Vista, Rio de Janeiro - RJ
locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Parque Nacional da Tijuca - Alto da Boa Vista, Rio de Janeiro - RJ")
print(location.altitude)
print(location.address)
print(location.latitude)
print(location.longitude)
print(location.point)
#print(location.raw)