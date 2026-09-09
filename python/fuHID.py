import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
from labellines import labelLine, labelLines

fuHID = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/fuHID2.txt', header=0, delimiter=';', na_values='-999')
bat = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/bat.txt', header=0, delimiter=';', na_values='-999')

# ~ print(fuHID)

fu_dry = fuHID.iloc[0:12]
fu_wet = fuHID.iloc[12:24]

fig, axs = plt.subplots(1,3,figsize=(11,2))

axs[0].set_title('a) Dry season \n (may-oct)', fontsize = 12)
axs[0].plot(fu_dry['hora'],fu_dry['hid'],color='#0000CD',linewidth=2.5,label='current', alpha = 0.8)
axs[0].plot(fu_dry['hora'],fu_dry['hidaj'],color='dodgerblue',linewidth=2.5,label='managed', alpha = 0.8)
axs[0].fill_between(fu_dry['hora'],fu_dry['solar'],color='#FBAA1B',linewidth=0,label='ajustada', alpha = 0.5)
axs[0].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[0].yaxis.set_tick_params(labelsize=10)
labelLines(axs[0].get_lines(), zorder=2.5, fontsize=12)
axs[0].set_ylabel('utilization factor [%]', fontsize=12)
axs[0].set_xlim(0, 11)
axs[0].set_ylim(0, 100)
axs[0].set_xlabel('hours', fontsize=12)

axs[1].set_title('b) Wet season \n (nov-abr)', fontsize = 12)
axs[1].plot(fu_wet['hora'],fu_wet['hid'],color='#0000CD',linewidth=2.5,label='current', alpha = 0.8)
axs[1].plot(fu_wet['hora'],fu_wet['hidaj'],color='dodgerblue',linewidth=2.5,label='managed', alpha = 0.8)
axs[1].fill_between(fu_wet['hora'],fu_wet['solar'],color='#FBAA1B',linewidth=0,label='ajustada', alpha = 0.5)
axs[1].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[1].yaxis.set_tick_params(labelsize=0, color='white')
labelLines(axs[1].get_lines(), zorder=2.5, fontsize=12)
# ~ axs[1].set_ylabel('disponibilidad [%]', fontsize=14)
axs[1].set_xlim(0, 11)
axs[1].set_ylim(0, 100)

axs[1].set_xlabel('hours', fontsize=12)

axs[2].set_title('c) Batteries', fontsize = 12)
axs[2].set_xlim(2022.5, 2050.5)
axs[2].bar(bat['anios'], bat['N'], color='#ADA4BA', width = 1)
axs[2].bar(bat['anios'], bat['C'], bottom=bat['N'], color='#FF9B9B', width = 1)
axs[2].bar(bat['anios'], bat['O'], bottom=bat['N']+bat['C'], color='#BCEE9B', width = 1)
axs[2].bar(bat['anios'], bat['S'], bottom=bat['N']+bat['C']+bat['O'], color='#D7B99B', width = 1)
axs[2].yaxis.tick_right()
axs[2].yaxis.set_label_position('right')
axs[2].set_ylabel('capacity [MW]', fontsize=12)
axs[2].set_xlabel('years', fontsize=12)
axs[2].tick_params(axis='x', rotation=90)


fig.text(0.8, 0.8,'Norte', fontsize=12)
fig.text(0.8, 0.8,'Centro', fontsize=12)
fig.text(0.8, 0.8,'Oriente', fontsize=12)
fig.text(0.8, 0.8,'Sur', fontsize=12)

fig.subplots_adjust(wspace=0.05)
plt.savefig('fu.svg', dpi=300, bbox_inches="tight")
