import requests
import folium
from geopy import distance

# Get the latitude and longitude coordinates of a location
def get_lat_long(location):
    url = "https://nominatim.openstreetmap.org/search?q={}&format=json&addressdetails=1&limit=1".format(location)
    response = requests.get(url).json()
    return (response[0]['lat'], response[0]['lon'])

pickup = get_lat_long("Marathahalli, Bangalore, India")
dropoff = get_lat_long("Indiranagar, Bangalore, India")

# Calculate the distance between the two locations using Geopy
pickup_coords = (float(pickup[0]), float(pickup[1]))
dropoff_coords = (float(dropoff[0]), float(dropoff[1]))

dist = distance.distance(pickup_coords, dropoff_coords).km

# Create a map using Folium
map = folium.Map(location=pickup, zoom_start=12)

# Add markers for the pickup and dropoff locations
folium.Marker(location=pickup, icon=folium.Icon(color='blue'), popup='Pickup').add_to(map)
folium.Marker(location=dropoff, icon=folium.Icon(color='red'), popup='Dropoff').add_to(map)

# Add a polyline between the pickup and dropoff locations
folium.PolyLine(locations=[(float(pickup[0]),float(pickup[1])),(float(dropoff[0]),float(dropoff[1]))]).add_to(map)
# Add a marker at the midpoint between the pickup and dropoff locations, displaying the distance between them
folium.Marker(location=((float(pickup[0]) + float(dropoff[0]))/2, (float(pickup[1]) + float(dropoff[1])/2)), icon=folium.Icon(color='purple'), popup='Distance: {:.2f} km'.format(dist)).add_to(map)

# Save the map to an HTML file
map.save('ny_map.html')
