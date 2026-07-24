import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/adiciones.txt', header=0, delimiter=',', na_values='-999')

fig, ax = plt.subplots(figsize=(6,4), sharey='row')
gs = fig.add_gridspec(2,2, wspace=0.1, hspace=0.5, height_ratios=[1, 0.6])

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title('BAU', fontsize = 13)
ax1.bar(ad['Anio'], ad['HidroT'], color='#0000CD', width=1)
ax1.bar(ad['Anio'], ad['EolicaT'], bottom=ad['HidroT'], color='#8FC73E', width=1)
ax1.bar(ad['Anio'], ad['SolarT'], bottom=ad['HidroT']+ad['EolicaT'], color='#FBAA1B', width=1)
ax1.legend(["Hydro","Wind","Solar"], frameon=False,bbox_to_anchor=(0.9, 0.9), borderaxespad=0.,fontsize=12)
ax1.set_xlim(2023, 2050)
# ~ ax1.set_ylabel('[MW]', fontsize=12)

ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title('ALT', fontsize = 13)
ax2.bar(ad['Anio'], ad['Hidro'], color='#0000CD', width=1)
ax2.bar(ad['Anio'], ad['Eolica'], bottom=ad['Hidro'], color='#8FC73E', width=1)
ax2.bar(ad['Anio'], ad['Solar'], bottom=ad['Hidro']+ad['Eolica'], color='#FBAA1B', width=1)
ax2.set_xlim(2023, 2050)

ax3 = fig.add_subplot(gs[1, :])
ax3.set_title('DS', fontsize = 13)
ax3.plot(ad['Anio'], ad['cien'], color='#FBAA1B', linewidth=2)
ax3.plot(ad['Anio'], ad['mil'], color='#FBAA1B')
ax3.fill_between(ad['Anio'], 0, ad['mil'], alpha=0.5, color='#FBAA1B', label='1000 MW')
ax3.fill_between(ad['Anio'], 0, ad['cien'], alpha=0.8, color='#FBAA1B', label='100 MW')
ax3.legend( frameon=False,bbox_to_anchor=(0.3, 0.4), borderaxespad=0.,fontsize=12)
ax3.set_xlim(2023, 2050)
ax3.set_ylim(0, 1000)

fig.text(0.04, 0.5, '[MW]', va='center' ,fontsize=12, rotation='vertical')  


fig.subplots_adjust(wspace=0.05)
plt.savefig('ad.svg', dpi=300, bbox_inches="tight")
