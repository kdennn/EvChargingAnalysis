import pandas as pd
import geopandas as gpd
from shapely import wkt

df = pd.read_csv("/data/charge_points.csv")
df['geometry'] = df['geometry'].apply(wkt.loads)

gdf = gpd.GeoDataFrame(df, geometry='geometry')

