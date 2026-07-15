import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from shapely.geometry.polygon import LinearRing
from matplotlib.patches import Rectangle
import pandas as pd
import geopandas as gpd

Bolivia = gpd.read_file('/home/emi/Documents/GENERIS/shapes/Mapa de limites departamentales de Bolivia/limites_departamentales.shp')
print(Bolivia)
Sur = Bolivia.iloc[[1, 5, 7]]
Sur = Sur.dissolve()
Norte = Bolivia.iloc[[0, 8]]
Norte = Norte.dissolve()
Centro = Bolivia.iloc[[2, 6]]
Centro = Centro.dissolve()
Oriente = Bolivia.iloc[[4]]
Pando = Bolivia.iloc[[3]]

#centro, norte, oriente, sur, pando
lats = [-17.48, -16.51, -17.88,-19.3,-11.03]
lons = [-66.16,-68.13,-63.17, -65.25,-66.03]

lat1, lat2, lat3, lat4, lat5 = -17.38, -16.51, -17.78,-19.3,-11.03
lon1, lon2, lon3, lon4, lon5 = -66.16,-68.13,-63.17, -65.25,-66.03
lat6 = -17.54
lat7 = -17.94

# Method 1: Define colors for specific provinces by name
province_colors = {
    'Chuquisaca': '#ADA4BA',  # Red
    'Tarija': '#ADA4BA',  # Teal
    'Potosi': '#ADA4BA',  # Blue
    'Oruro': '#ADA4BA',  # Light Salmon
    'Cochabamba': '#ADA4BA',  # Mint
    'La Paz': '#ADA4BA',  # Teal
    'Beni': '#ADA4BA',  # Blue
    'Santa Cruz': '#ADA4BA',  # Light Salmon
    'Pando': '#ADA4BA',  # Mint
}

province_column = 'nom_dep'

# Map colors to each province (use default color for unmapped provinces)
# ~ Bolivia['color'] = Bolivia[province_column].map(province_colors)

# Create the plot
fig, ax = plt.subplots( 1,1, figsize=(10, 10))
# ~ fig = plt.figure(figsize=(10, 10))
# ~ ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.plot(lons, lats, 'o', color='black', ms="18", zorder=1000)
# ~ ax.add_feature(cfeature.BORDERS, edgecolor='ivory')
ax.plot(lons, lats, 'o', color='darkviolet', ms="11", zorder=1000)

ax.plot([lon1, lon2], [lat1, lat2], color='midnightblue', linewidth=3.9, label = 'L1') #centro-norte
ax.plot([lon1, lon4], [lat1, lat4], color='midnightblue', linewidth=1.65, label = 'L3') #centro-sur
ax.plot([lon1, lon3], [lat1, lat3], color='midnightblue', linewidth=2.6, label = 'L2') #centro-oriente
# ~ ax.plot([lon2, lon5], [lat2, lat5], color='midnightblue', linewidth=2, label = 'L4',linestyle='dashed') #norte-pando
ax.plot([lon2, lon3], [lat2, lat3], color='midnightblue', linewidth=0.6, label = 'L5') #oriente-norte
ax.plot([lon1, lon3], [lat6, lat7], color='midnightblue', linewidth=5, label = 'L6') #oriente-norte

# ~ ax.plot([lon1, lon2], [lat1, lat2], color='midnightblue', linewidth=3.9, label = 'L1 - 390 MW') #centro-norte
# ~ ax.plot([lon1, lon4], [lat1, lat4], color='midnightblue', linewidth=1.65, label = 'L3 - 165 MW') #centro-sur
# ~ ax.plot([lon1, lon3], [lat1, lat3], color='midnightblue', linewidth=2.6, label = 'L2 - 260 MW') #centro-oriente
# ~ ax.plot([lon2, lon5], [lat2, lat5], color='midnightblue', linewidth=2, label = 'L4',linestyle='dashed') #norte-pando
# ~ ax.plot([lon2, lon3], [lat2, lat3], color='midnightblue', linewidth=0.35, label = 'L5 - 35 MW') #oriente-norte
# ~ ax.plot([lon1, lon3], [lat6, lat7], color='midnightblue', linewidth=5, label = 'L6 - 500 MW') #oriente-norte
ax.tick_params(axis='both', labelsize=0, color='white')
# ~ ax.text(-66,-20, 'Sur',labelsize=10, color='white' )
ax.text(-66,-21, 'Sur',fontsize=20, weight = 'bold', color='black')
ax.text(-62,-18, 'Oriente',fontsize=20, weight = 'bold', color='black')
ax.text(-67.5,-14.5, 'Norte',fontsize=20, weight = 'bold', color='black')
ax.text(-68.7,-11.7, 'Pando',fontsize=20, weight = 'bold', color='black')
ax.text(-68.7,-19, 'Centro',fontsize=20, weight = 'bold', color='black')
ax.tick_params(axis='both', labelsize=24)
ax.set_yticks([-10, -14, -18, -22])
ax.set_xticks([-68, -64, -60])
# ~ ax.set_yticks([-10, -14, -18, -22])
# ~ ax.set_xticks([-68, -64, -60])
ax.set_ylabel('lat [°]', fontsize=24)
ax.set_xlabel('lon [°]', fontsize=24)

# ~ plt.legend(loc='upper right', fontsize = 15,frameon=False) 

# ~ Bolivia.plot(ax=ax, color=Bolivia['color'], linewidth=0, alpha=0.7,edgecolor='ivory')

# ~ Sur.plot(ax=ax, color='lightsteelblue', linewidth=4, alpha=0.7,edgecolor='white')
# ~ Norte.plot(ax=ax, color='lightsteelblue', linewidth=4, alpha=0.7,edgecolor='white')
# ~ Centro.plot(ax=ax, color='lightsteelblue', linewidth=4, alpha=0.7,edgecolor='white')
# ~ Oriente.plot(ax=ax, color='lightsteelblue', linewidth=4, alpha=0.7,edgecolor='white')
# ~ Pando.plot(ax=ax, color='lightsteelblue', linewidth=4, alpha=0.7,edgecolor='white')

# ~ Sur.plot(ax=ax, color='#A1140B', linewidth=2, alpha=0.8,edgecolor='whitesmoke')
Sur.plot(ax=ax, color='#D7B99B', linewidth=2,edgecolor='#C48888')

# ~ Norte.plot(ax=ax, color='#ADA4BA', linewidth=2, alpha=0.8,edgecolor='#C48888 ')
Norte.plot(ax=ax, color='#ADA4BA', linewidth=2,edgecolor='#C48888')

# ~ Centro.plot(ax=ax, color='#FF9B9B', linewidth=2, alpha=0.8,edgecolor='#C48888 ')
Centro.plot(ax=ax, color='#FF9B9B', linewidth=2,edgecolor='#C48888')

# ~ Oriente.plot(ax=ax, color='#8FC73E', linewidth=2, alpha=0.8,edgecolor='#C48888 ')
Oriente.plot(ax=ax, color='#BCEE9B', linewidth=2, edgecolor='#C48888')

# ~ Pando.plot(ax=ax, color='#36495A', linewidth=2, alpha=0.8,edgecolor='#C48888 ')
Pando.plot(ax=ax, color='#9BBC9B', linewidth=2, edgecolor='#C48888')

plt.savefig('mapas.png', dpi=600, bbox_inches="tight")

# ~ plt.show()
