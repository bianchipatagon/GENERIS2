import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/emisiones2.txt', header=0, delimiter=';', na_values='-999')
print(ad)
ad45 = ad.iloc[0:21]
ad50 = ad.iloc[21:26]
print(ad50)
fig = plt.figure(figsize=(5.5, 3))
gs = gridspec.GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[:, 0])  # All rows, first column
ax1.plot(ad45['Anio'], ad45['Tend'], color='#A1140B', label='BAU')
ax1.plot(ad45['Anio'], ad45['TendGD'], color='#A1140B', alpha=0.7, label='BAU-SD')
ax1.plot(ad45['Anio'], ad45['Alt'], color='#A1140B', alpha=0.4, label='ALT')
ax1.plot(ad45['Anio'], ad45['AltGD'], color='#A1140B', alpha=0.2, label='ALT-SD')
# ~ ax1.plot(ad45['Anio'], ad45['AltGDM'], color='#A1140B', alpha=0.2, label='ALT-GDM', linestyle='dashed')
ax1.set_ylabel('GHG emissions \n [10^3 CO$_2$e]', fontsize=13)
ax1.set_xlim(2025, 2045)
ax1.legend( frameon=False,bbox_to_anchor=(0.5, 0.7), borderaxespad=0.,fontsize=10)

ax2 = fig.add_subplot(gs[0, 1]) 
ax2.plot(ad50['Anio'], ad50['Tend'], color='#A1140B')
ax2.plot(ad50['Anio'], ad50['TendGD'], color='#A1140B', alpha=0.7)
ax2.xaxis.set_tick_params(labelsize=0, colors='white')

ax2.set_xlim(2046, 2050)

ax3 = fig.add_subplot(gs[1, 1]) 
ax3.plot(ad50['Anio'], ad50['Alt'], color='#A1140B', alpha=0.4)
ax3.plot(ad50['Anio'], ad50['AltGD'], color='#A1140B', alpha=0.2)
# ~ ax3.plot(ad50['Anio'], ad50['AltGDM'], color='#A1140B', alpha=0.2, linestyle='dashed')

ax3.set_xlim(2046, 2050)

# ~ axs[2].legend( frameon=False,bbox_to_anchor=(0.4, 0.7), borderaxespad=0.,fontsize=10)

fig.subplots_adjust(wspace=0.3)

plt.savefig('emis.svg', dpi=300, bbox_inches="tight")
