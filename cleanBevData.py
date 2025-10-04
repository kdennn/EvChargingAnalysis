import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt  # Import matplotlib
import geodatasets
import folium
from shapely.geometry import box

df = pd.read_csv('data/Georeferenzierte_BevDaten_2021.csv', sep=';')


# Extract coordinates from 'Gitter_ID_1km' string
# Parse out the parts after the N and E
def parseText(oldCord):
    # Remove prefix and split
    # CRS3035RES1000mN{north}E{east}
    parts = oldCord.replace("CRS3035RES1000mN", "").split("E")
    northing = int(parts[0])
    easting = int(parts[1])
    return (easting, northing)

#Convert to boxes so matches to epsg 3035
def pointsToSquares(arg, size=500):
    return box(arg[0] - size / 2, arg[1] - size / 2, arg[0] + size / 2, arg[1] + size / 2)

#applly text parsing
df["coordinates"] = df['Gitter_ID_1km'].apply(parseText)

#create geometry column using x=east, y=north to point
df['geometry'] = df['coordinates'].apply(lambda x: pointsToSquares(x))

# turn it into a Geo dataframe and set it to EPSG 3035
gdf = gpd.GeoDataFrame(df, geometry='geometry')
gdf.set_crs(epsg=3035, inplace=True)

ax = gdf.plot(column='Einwohner', legend=True, cmap='hot')






plt.show()
