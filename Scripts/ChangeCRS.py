import glob
import os
import numpy as np
import numba
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString, Polygon, MultiPoint
from shapely import speedups
speedups.enabled

files = glob.glob("D:pflow/through-pt/*.csv")

for i, filename in enumerate(files):
    print(i)
    df = pd.read_csv(filename)
    geometry = [Point(xy) for xy in zip(df.E, df.F)]
    df_name = df.D
    crs = {'init': 'epsg:4326'}
    gdf = gpd.GeoDataFrame(df_name, crs=crs, geometry=geometry)

    gdf = gdf.to_crs(epsg = 2449)
    df.E = gdf.geometry.x
    df.F = gdf.geometry.y
    path = "D:pflow/through-pt-2449/" + filename[-12:-4] + ".csv"
    df.to_csv(path)