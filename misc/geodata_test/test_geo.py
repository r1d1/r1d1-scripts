#!/usr/bin/env python3

import geopandas
import matplotlib.pyplot as plt

print(geopandas.__version__)

path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)

print(gdf)

gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["boundary"] = gdf.boundary
gdf["centroid"] = gdf.centroid

#gdf.plot("area", legend=True)
gdf.explore("area", legend=False)
plt.show()
