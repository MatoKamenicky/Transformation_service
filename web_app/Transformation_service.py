
import pyproj
from . import write_to_DB
#import write_to_DB

def transform_coordinates(x, y, z, from_epsg, to_epsg):
    # Create a transformer from the source CRS to the target CRS
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    lon, lat, height = transformer.transform(x, y, z)
    write_to_DB.write2db(lon,lat)
    
    return lon, lat, height


"""
# Example coordinates in EPSG 5514 with height
x_5514, y_5514, z_5514 = 123456, 789012, 100  # Example height in meters

from_epsg = 5514
to_epsg   = 4326

# Transform to EPSG 4326 with height
lon_4326, lat_4326, height_4326 = transform_coordinates(x_5514, y_5514, z_5514, from_epsg, to_epsg)

print(f'Original coordinates (EPSG 5514): {x_5514}, {y_5514}, {z_5514}')
print(f'Transformed coordinates (EPSG 4326): {lon_4326}, {lat_4326}, {height_4326}')

"""




