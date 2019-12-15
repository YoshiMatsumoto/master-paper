import glob
import os
import numpy as np
import numba
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString, Polygon, MultiPoint
from shapely import speedups
speedups.enabled


files = glob.glob("D:pflow/stop-pt/*.csv")

dist = gpd.read_file("D:pflow/range.geojson")
dist = dist.to_crs(epsg=2449)
all_gdf = []
l = 0
n = 0
for i, filename in enumerate(files):
    df = pd.read_csv(filename, names=["start_time", "duration", "X", "Y"])
    df["id"] = filename[-12:-4]
    df = df[['id','start_time','duration','X', 'Y']]
    geometry = [Point(xy) for xy in zip(df.X, df.Y)]
    df_name = df.drop(["X", "Y"], axis= 1)
    crs = {'init': 'epsg:2449'}
    gdf = gpd.GeoDataFrame(df_name, crs=crs, geometry=geometry)

    pip_mask = gdf.within(dist.at[0, 'geometry'])
    pip_data = gdf.loc[pip_mask]

    if len(pip_data) > 0:
        l += len(pip_data)
        n += 1
        all_gdf.extend(pip_data.values)
        # path = "D:pflow/" + filename[-12:-4] + ".geojson"
        # pip_data.to_file(path, driver='GeoJSON')
    else:
        pass

df_all = pd.DataFrame(all_gdf, columns=['id','start_time','duration', 'geometry'])
crs = {'init': 'epsg:2449'}
gdf_all = gpd.GeoDataFrame(df_all, crs=crs)
path = "D:pflow/" +"stop-pt-clip.geojson"
gdf_all.to_file(path, driver='GeoJSON')
print(l/n)