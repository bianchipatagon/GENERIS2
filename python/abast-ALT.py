import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ALT = pd.read_csv('abastALT.txt', header=0, delimiter=';', na_values='-999')
CUR = pd.read_csv('curt.txt', header=0, delimiter=';', na_values='-999')
CUR.loc[:, CUR.columns != 'hora'] *= -1
CUR['hora_label'] = CUR['hora'].str.replace(r'^(Dry|Wet):', '', regex=True)
LOAD = pd.read_csv('load.txt', header=0, delimiter=';', na_values='-999')

# ~ print(CUR)
fig, axs = plt.subplots(2,4,figsize=(13.5,3),gridspec_kw={'height_ratios': [3, 1]}, sharey='row', sharex='row')

#################### ALT ###############################
################### NORTE
axs[0,0].set_title('Norte', fontsize = 14, bbox=dict(facecolor='#ADA4BA', edgecolor='none', boxstyle='round,pad=0.3'))
axs[0,0].bar(ALT['hora'], ALT['FosilN'], color='black', alpha=0.8, width = 1)
axs[0,0].bar(ALT['hora'], ALT['HidroN'], bottom=ALT['FosilN'], color='#0000CD', alpha=0.8, width = 1)
axs[0,0].bar(ALT['hora'], ALT['EolicoN'], bottom=ALT['FosilN']+ALT['HidroN'], color='#8FC73E', alpha=0.8, width = 1)
axs[0,0].bar(ALT['hora'], ALT['ImpoN'], bottom=ALT['EolicoN']+ALT['FosilN']+ALT['HidroN'], color='#6D6F70', alpha=0.8, width = 1)
axs[0,0].bar(ALT['hora'], ALT['SolarN'], bottom=ALT['FosilN']+ALT['HidroN']+ALT['EolicoN']+ALT['ImpoN'], color='#FBAA1B', alpha=0.8, width = 1)
axs[0,0].bar(ALT['hora'], ALT['SolarDN'], bottom=ALT['SolarN']+ALT['ImpoN']+ALT['EolicoN']+ALT['FosilN']+ALT['HidroN'], color='#FBAA1B', alpha=0.8, width = 1, hatch='//')
# ~ axs[0,0].plot(ALT['hora'], ALT['ImpoN']+ALT['EolicoN']+ALT['FosilN']+ALT['HidroN']+ALT['SolarN'], color='magenta', linewidth = 2)
axs[0,0].plot(ALT['hora'], LOAD['loadN'], color='magenta', linewidth = 2)
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,0].yaxis.set_tick_params(labelsize=12)
axs[0,0].set_xlim(-0.5, 23.5)
axs[0,0].set_ylim(0,1400)
axs[0,0].set_xticks(range(0, len(ALT['hora']), 2))
axs[0,0].set_xticklabels(ALT['hora'][::2])
axs[0,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,0].xaxis.set_tick_params(labelsize=0, rotation=90, color='white')

################### CENTRO
axs[0,1].set_title('Centro', fontsize = 14, bbox=dict(facecolor='#FF9B9B', edgecolor='none', boxstyle='round,pad=0.3'))
axs[0,1].bar(ALT['hora'], ALT['FosilC'], color='black', alpha=0.8, width = 1)
axs[0,1].bar(ALT['hora'], ALT['HidroC'], bottom=ALT['FosilC'], color='#0000CD', alpha=0.8, width = 1)
axs[0,1].bar(ALT['hora'], ALT['EolicoC'], bottom=ALT['FosilC']+ALT['HidroC'], color='#8FC73E', alpha=0.8, width = 1)
axs[0,1].bar(ALT['hora'], ALT['ImpoC'], bottom=ALT['EolicoC']+ALT['FosilC']+ALT['HidroC'], color='#6D6F70', alpha=0.8, width = 1)
axs[0,1].bar(ALT['hora'], ALT['SolarC'], bottom=ALT['ImpoC']+ALT['EolicoC']+ALT['FosilC']+ALT['HidroC'], color='#FBAA1B', alpha=0.8, width = 1)
axs[0,1].bar(ALT['hora'], ALT['SolarDC'], bottom=+ALT['SolarC']+ALT['ImpoC']+ALT['EolicoC']+ALT['FosilC']+ALT['HidroC'], color='#FBAA1B', alpha=0.8, width = 1, hatch='//')
# ~ axs[0,1].plot(ALT['hora'], ALT['ImpoC']+ALT['EolicoC']+ALT['FosilC']+ALT['HidroC']+ALT['SolarC'], color='magenta', linewidth = 2)
axs[0,1].plot(ALT['hora'], LOAD['loadC'], color='magenta', linewidth = 2)
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,1].set_xticks(range(0, len(ALT['hora']), 2))
axs[0,1].set_xticklabels(ALT['hora'][::2])
axs[0,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,1].xaxis.set_tick_params(labelsize=0, rotation=90, color='white')
axs[0,1].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')

################### ORIENTE
axs[0,2].set_title('Oriente', fontsize = 14, bbox=dict(facecolor='#BCEE9B', edgecolor='none', boxstyle='round,pad=0.3'))
axs[0,2].bar(ALT['hora'], ALT['FosilO'], color='black', alpha=0.8, width = 1)
axs[0,2].bar(ALT['hora'], ALT['HidroO'], bottom=ALT['FosilO'], color='#0000CD', alpha=0.8, width = 1)
axs[0,2].bar(ALT['hora'], ALT['SolarO'], bottom=ALT['FosilO']+ALT['HidroO'], color='#FBAA1B', alpha=0.8, width = 1)
axs[0,2].bar(ALT['hora'], ALT['EolicoO'], bottom=ALT['FosilO']+ALT['HidroO']+ALT['SolarO'], color='#8FC73E', alpha=0.8, width = 1)
axs[0,2].bar(ALT['hora'], ALT['ImpoO'], bottom=ALT['EolicoO']+ALT['FosilO']+ALT['HidroO']+ALT['SolarO'], color='#6D6F70', alpha=0.8, width = 1)
axs[0,2].bar(ALT['hora'], ALT['SolarDO'], bottom=+ALT['SolarO']+ALT['ImpoO']+ALT['EolicoO']+ALT['FosilO']+ALT['HidroO'], color='#FBAA1B', alpha=0.8, width = 1, hatch='//')
# ~ axs[0,2].plot(ALT['hora'], ALT['ImpoO']+ALT['EolicoO']+ALT['FosilO']+ALT['HidroO']+ALT['SolarO'], color='magenta', linewidth = 2)
axs[0,2].plot(ALT['hora'], LOAD['loadO'], color='magenta', linewidth = 2)
axs[0,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,2].set_xticks(range(0, len(ALT['hora']), 2))
axs[0,2].set_xticklabels(ALT['hora'][::2])
axs[0,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,2].xaxis.set_tick_params(labelsize=0, rotation=90, color='white')
axs[0,2].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')

################### SUR
axs[0,3].set_title('Sur', fontsize = 14, bbox=dict(facecolor='#D7B99B', edgecolor='none', boxstyle='round,pad=0.3'))
axs[0,3].bar(ALT['hora'], ALT['FosilS'], color='black', alpha=0.8, width = 1)
axs[0,3].bar(ALT['hora'], ALT['HidroS'], bottom=ALT['FosilS'], color='#0000CD', alpha=0.8, width = 1)
axs[0,3].bar(ALT['hora'], ALT['SolarS'], bottom=ALT['FosilS']+ALT['HidroS'], color='#FBAA1B', alpha=0.8, width = 1)
axs[0,3].bar(ALT['hora'], ALT['EolicoS'], bottom=ALT['FosilS']+ALT['HidroS']+ALT['SolarS'], color='#8FC73E', alpha=0.8, width = 1)
axs[0,3].bar(ALT['hora'], ALT['ImpoS'], bottom=ALT['EolicoS']+ALT['FosilS']+ALT['HidroS']+ALT['SolarS'], color='#6D6F70', alpha=0.8, width = 1)
axs[0,3].bar(ALT['hora'], ALT['SolarDS'], bottom=+ALT['SolarS']+ALT['ImpoS']+ALT['EolicoS']+ALT['FosilS']+ALT['HidroS'], color='#FBAA1B', alpha=0.8, width = 1, hatch='//')
# ~ axs[0,3].plot(ALT['hora'], ALT['ImpoS']+ALT['EolicoS']+ALT['FosilS']+ALT['HidroS']+ALT['SolarS'], color='magenta', linewidth = 2)
axs[0,3].plot(ALT['hora'], LOAD['loadS'], color='magenta', linewidth = 2)

axs[0,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,3].legend(["Demand","Hydro","Wind","Import", "Solar Dist.","Fossil","Solar"], frameon=False,bbox_to_anchor=(0.2, 0.8), loc='center left', borderaxespad=0.,fontsize=9, ncols = 2)
# ~ axs[0,3].legend(["Fósil", "Hidro","Solar","Eólica"], frameon=False,bbox_to_anchor=(-2, -1.6), loc='center left', borderaxespad=0.,fontsize=12, ncols=4)

axs[0,3].set_xticks(range(0, len(ALT['hora']), 2))
axs[0,3].set_xticklabels(ALT['hora'][::2])
axs[0,3].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,3].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,3].xaxis.set_tick_params(labelsize=0, rotation=90, color='white')
axs[0,3].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')


#################### Vertido ###############################
################### NORTE
cols = ['HidroN', 'SolarN', 'EolicoN']
colors = ['#0000CD', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = CUR[cols].clip(lower=0)  # keep only positive values
neg_data = CUR[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(CUR))
neg_bottoms = N.zeros(len(CUR))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,0].bar(CUR['hora'], pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,0].bar(CUR['hora'], neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8, width=1)
    neg_bottoms += neg_data[col].values

axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,0].set_ylim(-600, 0)
axs[1,0].yaxis.set_tick_params(labelsize=12)
axs[1,0].set_xticks(range(0, len(CUR['hora']), 2))
axs[1,0].set_xticklabels(CUR['hora_label'][::2])
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')

################### CENTRO
cols = ['HidroC', 'SolarC', 'EolicoC']
colors = ['#0000CD', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = CUR[cols].clip(lower=0)  # keep only positive values
neg_data = CUR[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(CUR))
neg_bottoms = N.zeros(len(CUR))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,1].bar(CUR['hora'], pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,1].bar(CUR['hora'], neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8, width=1)
    neg_bottoms += neg_data[col].values

axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')
# ~ axs[1,1].set_ylim(-400, 0)
axs[1,1].yaxis.set_tick_params(labelsize=12)
axs[1,1].set_xticks(range(0, len(CUR['hora']), 2))
axs[1,1].set_xticklabels(CUR['hora_label'][::2])
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,1].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')

################### ORIENTE
cols = ['HidroO', 'SolarO', 'EolicoO']
colors = ['#0000CD', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = CUR[cols].clip(lower=0)  # keep only positive values
neg_data = CUR[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(CUR))
neg_bottoms = N.zeros(len(CUR))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,2].bar(CUR['hora'], pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,2].bar(CUR['hora'], neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8, width=1)
    neg_bottoms += neg_data[col].values

axs[1,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')
# ~ axs[1,2].set_ylim(-400, 0)
axs[1,2].yaxis.set_tick_params(labelsize=12)
axs[1,2].set_xticks(range(0, len(CUR['hora']), 2))
axs[1,2].set_xticklabels(CUR['hora_label'][::2])
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,2].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')

################### SUR
cols = ['HidroS', 'SolarS', 'EolicoS']
colors = ['#0000CD', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = CUR[cols].clip(lower=0)  # keep only positive values
neg_data = CUR[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(CUR))
neg_bottoms = N.zeros(len(CUR))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,3].bar(CUR['hora'], pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,3].bar(CUR['hora'], neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8, width=1)
    neg_bottoms += neg_data[col].values

axs[1,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,3].axhline(linewidth=1, color='black', label='_nolegend_')
# ~ axs[1,3].set_ylim(-400, 0)
axs[1,3].yaxis.set_tick_params(labelsize=12)
axs[1,3].set_xticks(range(0, len(CUR['hora']), 2))
axs[1,3].set_xticklabels(CUR['hora_label'][::2])
axs[1,3].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,3].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,3].yaxis.set_tick_params(labelsize=0, rotation=90, color='white')

fig.subplots_adjust(wspace=0.05, hspace=0.1)

fig.text(0.91, 0.69, 'Regional \nsupply', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.91, 0.3, 'Power \ncurtailment', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.08, 0.5, '[MW]', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.1,0.9,'dry \nseason',fontsize=10)
fig.text(0.15,0.9,'wet \nseason',fontsize=10)
fig.text(0.5,-0.15,'hours',fontsize=12)
fig.text(0.45,1,'ALT-DS year:2050',fontsize=14)

plt.savefig('abastALT.svg', dpi=300, bbox_inches="tight")
