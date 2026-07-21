import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
from labellines import labelLine, labelLines

fuHID = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/fuHID.txt', header=0, delimiter=',', na_values='-999')

# ~ print(fuHID)

fu_dry = fuHID.iloc[0:12]
fu_wet = fuHID.iloc[12:24]

fig, axs = plt.subplots(1,2,figsize=(7,2),sharex=True, sharey=True)

axs[0].set_title('Dry season \n (may-oct)', fontsize = 14)
axs[0].plot(fu_dry['hora'],fu_dry['hid'],color='#A1150B',linewidth=2.5,label='current', alpha = 0.8)
axs[0].plot(fu_dry['hora'],fu_dry['hidaj'],color='#0000CD',linewidth=2.5,label='managed', alpha = 0.8)
axs[0].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[0].yaxis.set_tick_params(labelsize=10)
labelLines(axs[0].get_lines(), zorder=2.5, fontsize=12)
axs[0].set_ylabel('availability [%]', fontsize=12)
axs[0].set_xlim(0, 11)
axs[0].set_xlabel('hours', fontsize=12)

axs[1].set_title('Humid season \n (nov-apr)', fontsize = 14)
axs[1].plot(fu_wet['hora'],fu_wet['hid'],color='#A1150B',linewidth=2.5,label='current', alpha = 0.8)
axs[1].plot(fu_wet['hora'],fu_wet['hidaj'],color='#0000CD',linewidth=2.5,label='managed', alpha = 0.8)
axs[1].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[1].yaxis.set_tick_params(labelsize=0, color='white')
labelLines(axs[1].get_lines(), zorder=2.5, fontsize=12)
# ~ axs[1].set_ylabel('disponibilidad [%]', fontsize=14)
axs[1].set_xlim(0, 11)
axs[1].set_xlabel('hours', fontsize=12)

fig.subplots_adjust(wspace=0.05)
plt.savefig('fu.svg', dpi=300, bbox_inches="tight")
