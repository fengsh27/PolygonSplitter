from shapely.geometry import shape, LineString, mapping
from shapely.ops import split, linemerge, unary_union, polygonize
import geojson  

def cut_polygon_by_line(polygon, line):
    merged = linemerge([polygon.boundary, line])
    borders = unary_union(merged)
    polygons = polygonize(borders)
    return list(polygons)

def plot(shapely_objects, figure_path='fig.png'):
    from matplotlib import pyplot as plt
    import geopandas as gpd
    boundary = gpd.GeoSeries(shapely_objects)
    boundary.plot(color=['red', 'green', 'blue', 'yellow', 'yellow'])
    plt.savefig(figure_path)
