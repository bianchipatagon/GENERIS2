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
import numpy as np

Bolivia = gpd.read_file('/home/emi/Documents/GENERIS/shapes/Mapa de limites departamentales de Bolivia/limites_departamentales.shp')
# ~ print(Bolivia)
Sur = Bolivia.iloc[[1, 5, 7]]
Sur = Sur.dissolve()
Norte = Bolivia.iloc[[0, 8]]
Norte = Norte.dissolve()
Centro = Bolivia.iloc[[2, 6]]
Centro = Centro.dissolve()
Oriente = Bolivia.iloc[[4]]
Pando = Bolivia.iloc[[3]]



lats = [-14,-17.48, -17.88,-20.3]
lons = [-67.13,-66.16,-62, -65.25]
lonsS = [-69.13,-68.16,-64, -67.25]

#N, C, O, S
valuesD =[1340,1326,2463,1069]
valuesT =[88,900,1041,545]
valuesH =[309.7,420.5,0,27.9]
valuesV =[0,27,108,0]
valuesS =[0,50,0,64]

# Convert everything to numpy arrays first
lons   = np.asarray(lons,   dtype=float)
lats   = np.asarray(lats,   dtype=float)
valuesD = np.asarray(valuesD, dtype=float)
valuesT = np.asarray(valuesT, dtype=float)
valuesH = np.asarray(valuesH, dtype=float)
valuesV = np.asarray(valuesV, dtype=float)
valuesS = np.asarray(valuesS, dtype=float)

# --- size scaling (tweak s_scale to taste) ---
s_scaleD = 3                         # area units per data unit
s_scale = 8  
sizesD   = valuesD * s_scaleD             # passed to scatter(s=...)
sizesT   = valuesT * s_scale             # passed to scatter(s=...)
sizesH   = valuesH * s_scale             # passed to scatter(s=...)
sizesV   = valuesV * s_scale             # passed to scatter(s=...)
sizesS   = valuesS * s_scale             # passed to scatter(s=...)

fig, (ax1, ax2, ax3,ax4) = plt.subplots(1,4,figsize=(18, 7),subplot_kw={"projection": ccrs.PlateCarree()},)

#####
ax1.tick_params(axis='both', labelsize=0, color='white')
ax1.text(-59,-11.5, 'a)', fontsize=24)
ax1.set_title('Power demand \n [kBEP]' , fontsize=20)
Sur.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax1, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax1.scatter(
    lons, lats,
    s          = sizesD,         # marker area (in points²)
    color="#6D6F70",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesD):
    ax1.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 16,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax2.set_title('Thermal \n [MW]' , fontsize=20)
ax2.text(-59,-11.5, 'b)', fontsize=24)
ax2.tick_params(axis='both', labelsize=0, color='white')
Sur.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax2, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax2.scatter(
    lons, lats,
    s          = sizesT,         # marker area (in points²)
    color="#8B4513",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesT):
    ax2.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 16,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax3.tick_params(axis='both', labelsize=0, color='white')
ax3.set_title('Hydro \n [MW]', fontsize=20)
ax3.text(-59,-11.5, 'c)', fontsize=24)
Sur.plot(ax=ax3, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax3, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax3, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax3, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax3, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax3.scatter(
    lons, lats,
    s          = sizesH,         # marker area (in points²)
    color="#0000CD",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesH):
    ax3.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 16,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax4.tick_params(axis='both', labelsize=0, color='white')
ax4.set_title('Wind & Solar \n [MW]', fontsize=20)
ax4.text(-59,-11.5, 'd)', fontsize=24)

Sur.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax4, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax4.scatter(
    lons, lats,
    s          = sizesV,         # marker area (in points²)
    color="#9ACD32",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
sc = ax4.scatter(
    lonsS, lats,
    s          = sizesS,         # marker area (in points²)
    color="#FBAA1B",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesV):
    ax4.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 16,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
    
for lon, lat, val in zip(lonsS, lats, valuesS):
    ax4.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 16,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )

fig.subplots_adjust(wspace=0.05, hspace=0.1)

plt.savefig('mapas3.svg', dpi=600, bbox_inches="tight")

# ~ plt.show()
