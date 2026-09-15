import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
from labellines import labelLine, labelLines

perc = pd.read_csv('percent.txt', header=0, delimiter=';', na_values='-999')
fload = pd.read_csv('fload.txt', header=0, delimiter=';', na_values='-999')

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(8,2))

ax3 = ax1.twinx()

ax1.set_xlim(2023, 2050)
ax1.bar(perc['Anio'], perc['Fosil'], color='black', alpha=0.8, width = 1)
ax1.bar(perc['Anio'], perc['Hidro'], bottom=perc['Fosil'], color='#0000CD', alpha=0.8, width = 1)
ax1.bar(perc['Anio'], perc['Eolico'], bottom=perc['Fosil']+perc['Hidro'], color='#8FC73E', alpha=0.8, width = 1)
ax1.bar(perc['Anio'], perc['Solar'], bottom=perc['Fosil']+perc['Hidro']+perc['Eolico'], color='#FBAA1B', alpha=0.8, width = 1)
ax1.bar(perc['Anio'], perc['SolarD'], bottom=perc['Fosil']+perc['Hidro']+perc['Eolico']+perc['Solar'], color='#FBAA1B', alpha=0.8, width = 1, hatch='//')
ax1.set_ylabel('capacity [%]', fontsize=12)

ax3.plot(perc['Anio'], perc['Demanda'], color='magenta', linewidth = 2.5)
ax3.tick_params(axis='y', colors='magenta')
ax3.set_ylabel('demand [%]', fontsize=12, color='magenta')

ax2.set_xlim(2023, 2050)
ax2.set_ylim(0, 32)
ax2.plot(fload['anio'], fload['fload']*100, color='black', linewidth = 2.5)
ax2.fill_between(fload['anio'], fload['fload']*100, facecolor='none', edgecolor='black',  hatch='//', linewidth=0.0) 
ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()
ax2.set_ylabel('thermal \nfactor load [%]', fontsize=12)

fig.text(0.15,0.75,'a)',fontsize=12)
fig.text(0.60,0.75,'b)',fontsize=12)

fig.subplots_adjust(wspace=0.3)
plt.savefig('perc.png', dpi=300, bbox_inches="tight")
