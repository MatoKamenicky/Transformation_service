import pyproj
#from . import write_to_DB
#import write_to_DB

def transform_coordinates_2D(x, y):
    # Create a transformer from the source CRS to the target CRS
    from_epsg = 8352
    to_epsg   = 4326
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    lon, lat = transformer.transform(x, y)
    input = [x,y]
    output = [lon,lat]
    #write_to_DB.write2db(input,output)
    
    return lon, lat


def transform_coordinates_3D(x, y, z):
    # Create a transformer from the source CRS to the target CRS
    from_epsg = 8352
    to_epsg   = 4326
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    lon, lat = transformer.transform(x, y)
    h = 100
    input = [x,y,z]
    output = [lon,lat,h]
    #write_to_DB.write2db(input,output)
    
    return lon, lat, h




