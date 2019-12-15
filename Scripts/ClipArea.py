import glob
import os
import numpy as np
import numba
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon, MultiPoint
from shapely import speedups
speedups.enabled

dist = gpd.read_file("D:pflow/range.geojson")
dist = dist.to_crs(epsg=4326)

files = glob.glob("D:pflow/p-csv/**/*.csv")

for i, filename in enumerate(files):
    df = pd.read_csv(filename, names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N"])
    geometry = [Point(xy) for xy in zip(df.E, df.F)]
    df_name = df.D
    crs = {'init': 'epsg:4326'}
    gdf = gpd.GeoDataFrame(df_name, crs=crs, geometry=geometry)

    pip_mask = gdf.within(dist.at[0, 'geometry'])
    pip_data = gdf.loc[pip_mask]
    if len(pip_data) == 0:
        pass
    else:
        # path1 = "D:pflow/clip-pt/" + filename[-12:-4] + ".geojson"
        path2 = "D:pflow/through-pt/" + filename[-12:-4] + ".csv"
        df.to_csv(path2)
        # pip_data.to_file(path, driver='GeoJSON')
        print("Success")