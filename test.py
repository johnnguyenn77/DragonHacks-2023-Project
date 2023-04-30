import geocoder
g = geocoder.ip('me')
result = g.address
result = result.split(', ')
print(result[0])
print(g.latlng)
print(g.address)