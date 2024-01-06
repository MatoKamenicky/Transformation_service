import pyproj
from . import write_to_DB
#import write_to_DB

def transform_coordinates(x, y, z, from_epsg, to_epsg):
    # Create a transformer from the source CRS to the target CRS
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    lon, lat, height = transformer.transform(x, y, z)
    input = [x,y,z]
    output = [lon,lat,height]
    write_to_DB.write2db(input,output)
    
    return lon, lat, height




