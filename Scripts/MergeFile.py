import glob
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, MultiPoint, MultiLineString, LineString
%matplotlib inline

def WriteFile(mlns, filename):
    df = pd.DataFrame(mlns, columns = ["id", "pts"])
    crs = {'init': 'epsg:4326'}
    gdf = gpd.GeoDataFrame(df["id"], crs=crs, geometry = df["pts"])
    gdf.to_file(filename, driver='GeoJSON')

files = []
for f in glob.glob("hitono_nagare/2011_Weekday/p-csv/*/*.csv"):
    files.append(os.path.split(f)[1])

print("Finish File Reading")

all_sample = []
for file in files:
    name = file
    df = pd.read_csv(i, names=('A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'))
    mpt = MultiPoint([Point(xy) for xy in zip(df.E, df.F)][0:1440])
    one_sample = [name, mpt]
    all_sample.append(one_sample)

print("Finish Point Reading")

df = pd.DataFrame(all_sample, columns = ["id", "pts"])
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df["id"], crs=crs, geometry = df["pts"])
gdf.to_file("all_sample_mpt", driver='GeoJSON')

print("Finish All")