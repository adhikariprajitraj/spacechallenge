import geopandas as gpd, fiona
import matplotlib.pyplot as plt

fiona.drvsupport.supported_drivers['kml'] = 'rw' # enable KML support which is disabled by default
fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default


# Read the KML file
gdf = gpd.read_file("bioscape_domain_20220201.kml", driver='KML')

# Visualize the data
gdf.plot()
plt.title("Cape Floristic Region")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
