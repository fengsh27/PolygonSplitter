from shapely.geometry import shape, LineString, mapping
import geojson

from src.split_polygon import cut_polygon_by_line, plot

if __name__ == "__main__":
    with open('./data/room.geojson') as f:
        data = geojson.load(f)
        polygon = shape(data["geometry"])
        line = LineString([
            (-83.01771087384829,39.99526791339596,1588.6641999999993),
            (-83.01769735869483,39.995211565168965,1588.6641999999993),
        ])
        splitted_polygons = cut_polygon_by_line(polygon, line)
        plot(splitted_polygons, figure_path="./out/splitted_polygons.png")

        # output splitted polygons to geojson file
        geojson_polygons = [mapping(p) for p in splitted_polygons]

        with open('./out/splitted_polygons.geojson', 'w') as f:  
            geojson.dump(geojson.FeatureCollection(geojson_polygons), f)  

