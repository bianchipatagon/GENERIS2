import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import pandas as pd

potencia = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/generacion.txt', header=0, delimiter=';', na_values='-999')
print(potencia)

colors = ['black', '#FBAA1B','#FBAA1B','#8FC73E','#0000CD']
labels = ['Fossil','Solar','Solar Dist','Wind','Hydro']
hatch_patterns = ['', '','/', '', '']

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(1,5, figure=fig, width_ratios=[1,1.39,1.39,1.4,1.39])
# ~ gs = fig.add_gridspec(1, 5, wspace=0.1, hspace=0.3, width_ratios=[1,1.4,1.4])

ax1 = fig.add_subplot(gs[0])
ax1.pie(potencia['2025'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.2, wedgeprops=dict(width=0.98, edgecolor='white',alpha= 0.8), labeldistance=1.1,textprops=dict(color="black", fontsize=11), hatch=hatch_patterns)
ax1.set_title('2025 \n (11430 GWh)', fontsize=14)

ax2 = fig.add_subplot(gs[1])
ax2.pie(potencia['T2050'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.2,wedgeprops=dict(width=0.98, edgecolor='white',alpha= 0.8),labeldistance=1.1,textprops=dict(color="black", fontsize=11), hatch=hatch_patterns)
ax2.set_title('BAU 2050 \n (22410 GWh)', fontsize=14)

ax3 = fig.add_subplot(gs[2])
ax3.pie(potencia['T2050GD'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.2,wedgeprops=dict(width=0.98, edgecolor='white',alpha= 0.8),labeldistance=1.1,textprops=dict(color="black", fontsize=11), hatch=hatch_patterns)
ax3.set_title('BAU-SD 2050 \n (20610 GWh)', fontsize=14)

ax4 = fig.add_subplot(gs[3])
ax4.pie(potencia['A2050'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.2,wedgeprops=dict(width=0.98, edgecolor='white',alpha= 0.8),labeldistance=1.1,textprops=dict(color="black", fontsize=11), hatch=hatch_patterns)
ax4.set_title('ALT 2050 \n (22256 GWh)', fontsize=14)

ax5 = fig.add_subplot(gs[4])
ax5.pie(potencia['A2050GD'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.2,wedgeprops=dict(width=0.98, edgecolor='white',alpha= 0.8),labeldistance=1.1,textprops=dict(color="black", fontsize=11), hatch=hatch_patterns)
ax5.set_title('ALT-SD 2050 \n (22122 GWh)', fontsize=14)
ax5.legend(labels,  loc="center left",bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12, frameon=False)

fig.subplots_adjust(wspace=0.05)
plt.savefig('GENERACION.svg', dpi=300, bbox_inches="tight")
