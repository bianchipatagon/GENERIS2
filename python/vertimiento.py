import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimiento.txt', header=0, delimiter=';', na_values='-999')
print(ad)
fig, ax1 = plt.subplots(1,figsize=(5,2),sharex=True, sharey=True)
'''
ax1.bar(ad['anio'], ad['SolarT'], color='#FBAA1B')
ax1.bar(ad['anio'], ad['EolicaT'], bottom=ad['SolarT'], color='#8FC73E')
ax1.bar(ad['anio'], ad['HidroT'], bottom=ad['SolarT']+ad['EolicaT'], color='#207653')
ax1.legend(["Solar","Eólica","Hidro"], frameon=False,bbox_to_anchor=(0.2, 0.9), borderaxespad=0.,fontsize=10)
ax1.set_xlim(2022.5, 2050.5)
ax1.set_ylabel('[GWh]', fontsize=12)

ax3 = ax1.twinx()
ax3.plot(ad['anio'], ad['PorcT'])
'''
ax1.set_ylim(0, 4300)
ax1.set_xlim(2022.5, 2050.5)
ax1.bar(ad['anio'], ad['Solar'], color='#FBAA1B', alpha=0.8, width = 1)
ax1.bar(ad['anio'], ad['Eolica'], bottom=ad['Solar'], color='#8FC73E', alpha=0.8, width = 1)
ax1.bar(ad['anio'], ad['Hidro'], bottom=ad['Solar']+ad['Eolica'], color='#0000CD', alpha=0.8, width = 1)
ax1.set_ylabel('curtailment [GWh]', fontsize=12)
# ~ ax2.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])   
ax1.legend(["Solar","Wind","Hydro"], frameon=False,bbox_to_anchor=(0.23, 0.7), borderaxespad=0.,fontsize=10)

ax2 = ax1.twinx()
ax2.plot(ad['anio'], ad['Porc'],'.', color = 'orangered', markersize = 10)
ax2.set_ylabel('% renewables', fontsize=12, color='orangered')
ax2.tick_params(axis='y', colors='orangered')
# ~ ax2.set_ylim(0, 4300)

# ~ axs[2].legend( frameon=False,bbox_to_anchor=(0.4, 0.7), borderaxespad=0.,fontsize=10)

fig.subplots_adjust(wspace=0.1)

plt.savefig('vert.svg', dpi=300, bbox_inches="tight")
