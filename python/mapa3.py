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
valuesE =[0,0,261,0]
valuesS =[120,198,20,5]
valuesH =[205,291,0,0]
valuesE2 =[0,90,841,0]
valuesS2 =[320,588,20,632.5]
valuesH2 =[205,671,685,0]

# Convert everything to numpy arrays first
lons   = np.asarray(lons,   dtype=float)
lats   = np.asarray(lats,   dtype=float)
valuesE = np.asarray(valuesE, dtype=float)
valuesS = np.asarray(valuesS, dtype=float)
valuesH = np.asarray(valuesH, dtype=float)
valuesE2 = np.asarray(valuesE2, dtype=float)
valuesS2 = np.asarray(valuesS2, dtype=float)
valuesH2 = np.asarray(valuesH2, dtype=float)

# --- size scaling (tweak s_scale to taste) ---
s_scale = 20                           # area units per data unit
sizesE   = valuesE * s_scale             # passed to scatter(s=...)
sizesS   = valuesS * s_scale             # passed to scatter(s=...)
sizesH   = valuesH * s_scale             # passed to scatter(s=...)
sizesE2   = valuesE2 * s_scale             # passed to scatter(s=...)
sizesS2   = valuesS2 * s_scale             # passed to scatter(s=...)
sizesH2   = valuesH2 * s_scale             # passed to scatter(s=...)

fig, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2,3,figsize=(18, 14),subplot_kw={"projection": ccrs.PlateCarree()},)

#####
ax1.tick_params(axis='both', labelsize=0, color='white')
ax1.set_title('Wind', fontsize=30)
Sur.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax1, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax1, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax1.scatter(
    lons, lats,
    s          = sizesE,         # marker area (in points²)
    color="#8FC73E",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesE):
    ax1.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax2.tick_params(axis='both', labelsize=0, color='white')
ax2.set_title('BAU \n Solar', fontsize=30)

Sur.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax2, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax2, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax2.scatter(
    lons, lats,
    s          = sizesS,         # marker area (in points²)
    color="#FBAA1B",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesS):
    ax2.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax3.tick_params(axis='both', labelsize=0, color='white')
ax3.set_title('Hydro', fontsize=30)

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
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
        color = 'white'
    )
#####
ax4.tick_params(axis='both', labelsize=0, color='white')
Sur.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax4, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax4, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax4.scatter(
    lons, lats,
    s          = sizesE2,         # marker area (in points²)
    color="#8FC73E",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesE2):
    ax4.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax5.tick_params(axis='both', labelsize=0, color='white')
ax5.set_title('ALT', fontsize=30)

Sur.plot(ax=ax5, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax5, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax5, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax5, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax5, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax5.scatter(
    lons, lats,
    s          = sizesS2,         # marker area (in points²)
    color="#FBAA1B",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesS2):
    ax5.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
    )
#####
ax6.tick_params(axis='both', labelsize=0, color='white')
Sur.plot(ax=ax6, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Norte.plot(ax=ax6, color= 'white',linewidth=3, alpha=0.8,edgecolor='grey')
Centro.plot(ax=ax6, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Oriente.plot(ax=ax6, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')
Pando.plot(ax=ax6, color= 'white', linewidth=3, alpha=0.8,edgecolor='grey')

sc = ax6.scatter(
    lons, lats,
    s          = sizesH2,         # marker area (in points²)
    color="#0000CD",        # color encodes same variable (optional)
    cmap       = "plasma",
    alpha      = 0.75,
    edgecolors = "white",
    linewidths = 0.5,
    transform  = ccrs.PlateCarree(),  # ← always needed for lon/lat data
    zorder     = 5,
)
for lon, lat, val in zip(lons, lats, valuesH2):
    ax6.text(
        lon, lat-0.5,          # +1.5° nudges the label above the circle
        f"{val:.0f}",            # format to 1 decimal place
        fontsize      = 20,
        fontweight='bold',
        ha            = "center",
        va            = "bottom",
        transform     = ccrs.PlateCarree(),
        zorder        = 6,       # above the scatter circles
        color = 'white'
    )
fig.subplots_adjust(wspace=0.05, hspace=0.1)

plt.savefig('mapas3.svg', dpi=600, bbox_inches="tight")

# ~ plt.show()
