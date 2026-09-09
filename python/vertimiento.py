import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimiento.txt', header=0, delimiter=';', na_values='-999')
ad1 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimientom.txt', header=0, delimiter=';', na_values='-999')
ad2 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimientomb.txt', header=0, delimiter=';', na_values='-999')

print((ad2['Solar']+ad2['Eolica']+ad2['Hidro'])/ad1['Output'])
fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(12,2),sharex=True, sharey=True)
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

####
ax1.set_ylim(0, 4300)
ax1.set_xlim(2022.5, 2050.5)
ax1.bar(ad['anio'], ad['Solar'], color='#FBAA1B', alpha=0.8, width = 1)
ax1.bar(ad['anio'], ad['Eolica'], bottom=ad['Solar'], color='#8FC73E', alpha=0.8, width = 1)
ax1.bar(ad['anio'], ad['Hidro'], bottom=ad['Solar']+ad['Eolica'], color='#0000CD', alpha=0.8, width = 1)
ax1.set_ylabel('curtailment [GWh]', fontsize=12)
ax1.set_title('ALT-DS  ', fontsize=13)
ax1.text(2024, 3500, 'a)', fontsize=13)
# ~ ax1.legend(["Solar","Wind","Hydro"], frameon=False,bbox_to_anchor=(0.23, 0.7), borderaxespad=0.,fontsize=9)

ax4 = ax1.twinx()
ax5 = ax2.twinx()
ax6 = ax3.twinx()
ax5.sharey(ax4)
ax6.sharey(ax4)

ax4.plot(ad['anio'], ad['Porc'], color = 'orangered', linewidth=2)
ax4.plot(ad['anio'], ad['Porc'],'o', color = 'orangered', markersize = 6, mfc='white', markeredgewidth=2)
ax4.tick_params(axis='y', colors='orangered')
ax4.set_ylim(0, 40)          # propagates to ax5 and ax6
ax4.yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

# hide the right-hand tick labels on the inner twins, keep only ax6's
ax4.tick_params(axis='y', labelright=False)
ax5.tick_params(axis='y', labelright=False)

####

ax2.set_ylim(0, 4300)
ax2.set_xlim(2022.5, 2050.5)
ax2.bar(ad1['anio'], ad1['Solar'], color='#FBAA1B', alpha=0.8, width = 1)
ax2.bar(ad1['anio'], ad1['Eolica'], bottom=ad1['Solar'], color='#8FC73E', alpha=0.8, width = 1)
ax2.bar(ad1['anio'], ad1['Hidro'], bottom=ad1['Solar']+ad1['Eolica'], color='#0000CD', alpha=0.8, width = 1)
ax2.yaxis.set_tick_params(labelsize=0, rotation=90,color='white')
ax2.set_title('+ hydro management  ', fontsize=13)
ax2.text(2024, 3500, 'b)', fontsize=13)

ax5.plot(ad1['anio'], ((ad1['Solar']+ad1['Eolica']+ad1['Hidro'])/ad1['Output'])*100, color = 'orangered', linewidth=2)
ax5.plot(ad1['anio'],((ad1['Solar']+ad1['Eolica']+ad1['Hidro'])/ad1['Output'])*100,'o', color = 'orangered', markersize = 6, mfc='white', markeredgewidth=2)
ax5.tick_params(axis='y', colors='orangered')
ax5.yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

####

ax3.set_ylim(0, 4300)
ax3.set_xlim(2022.5, 2050.5)
ax3.bar(ad2['anio'], ad2['Solar'], color='#FBAA1B', alpha=0.8, width = 1)
ax3.bar(ad2['anio'], ad2['Eolica'], bottom=ad2['Solar'], color='#8FC73E', alpha=0.8, width = 1)
ax3.bar(ad2['anio'], ad2['Hidro'], bottom=ad2['Solar']+ad2['Eolica'], color='#0000CD', alpha=0.8, width = 1)
ax3.legend(["Solar","Wind","Hydro"], frameon=False,bbox_to_anchor=(0.23, 0.9), borderaxespad=0.,fontsize=12)
ax3.yaxis.set_tick_params(labelsize=0, rotation=90,color='white')
ax3.set_title('+ hydro management \n+ batteries  ', fontsize=13)
ax3.text(2024, 3500, 'c)', fontsize=13)

ax6.plot(ad1['anio'], ((ad2['Solar']+ad2['Eolica']+ad2['Hidro'])/ad1['Output'])*100, color = 'orangered', linewidth=2)
ax6.plot(ad1['anio'],((ad2['Solar']+ad2['Eolica']+ad2['Hidro'])/ad1['Output'])*100,'o', color = 'orangered', markersize = 6, mfc='white', markeredgewidth=2)
ax6.tick_params(axis='y', colors='orangered')
ax6.set_ylabel('% renewables', fontsize=12, color='orangered')


fig.subplots_adjust(wspace=0.05)

plt.savefig('vertimiento.svg', dpi=300, bbox_inches="tight")
