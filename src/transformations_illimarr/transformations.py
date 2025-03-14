from pyproj import Transformer

convert_to_lest = Transformer.from_crs("EPSG:4326", "EPSG:3301", always_xy=True)
convert_to_wgs = Transformer.from_crs("EPSG:3301", "EPSG:4326", always_xy=True)

def wgs84_to_lest97(lat, lon):
    y, x = convert_to_lest.transform(lon, lat)
    return round(x, 2), round(y, 2)

def lest97_to_wgs84(x, y):
    lon, lat = convert_to_wgs.transform(y, x)
    return round(lat, 6), round(lon, 6)
