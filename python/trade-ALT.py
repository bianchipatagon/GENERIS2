import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ALT = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
ALTGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
numeric_labels = ALT.index.str.split(':').str[1] 
print(numeric_labels)
ALT = -ALT
ALTGD = -ALTGD

RESTA1 = ALTGD-ALT
print(ALTGD)
print(ALT)
print(RESTA1)

fig, axs = plt.subplots(4,3,figsize=(9,4.5), sharey='row')

#################### IMPORTS ###############################
#################### ALT ###############################
################### 2030
##positivos
axs[2,0].bar(ALT.index, ALT['impoC30'], color='#FF9B9B', width =1)
axs[2,0].bar(ALT.index, ALT['impoN30'], bottom=ALT['impoC30'], color='#ADA4BA', width =1)
axs[2,0].bar(ALT.index, ALT['impoO30'], bottom=ALT['impoC30']+ALT['impoN30'], color='#BCEE9B', width =1)
axs[2,0].bar(ALT.index, ALT['impoS30'], bottom=ALT['impoC30']+ALT['impoN30']+ALT['impoO30'], color='#D7B99B', width =1)
axs[2,0].set_ylim(0, 700)
axs[2,0].set_xticks(range(0, len(ALT.index), 2))
axs[2,0].set_xticklabels(ALT.index[::2])
axs[2,0].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[2,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,0].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[2,0].yaxis.set_tick_params(labelsize=10)
axs[2,0].set_xlim(-0.5, 23.5)


################### 2040
axs[2,1].set_title('Imports', fontsize = 12)
##positivos
axs[2,1].bar(ALT.index, ALT['impoC40'], color='#FF9B9B', width =1)
axs[2,1].bar(ALT.index, ALT['impoN40'], bottom=ALT['impoC40'], color='#ADA4BA', width =1)
axs[2,1].bar(ALT.index, ALT['impoO40'], bottom=ALT['impoC40']+ALT['impoN40'], color='#BCEE9B', width =1)
axs[2,1].bar(ALT.index, ALT['impoS40'], bottom=ALT['impoC40']+ALT['impoN40']+ALT['impoO40'], color='#D7B99B', width =1)
axs[2,1].set_ylim(0, 700)
axs[2,1].set_xticks(range(0, len(ALT.index), 2))
axs[2,1].set_xticklabels(ALT.index[::2])
axs[2,1].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[2,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,1].tick_params(axis='both', labelsize=0, color='white')
axs[2,1].set_xlim(-0.5, 23.5)

# ~ axs[0,1].set_xlim(-0.5, 23.5)


################### 2050
# ~ axs[2,2].set_title('2050', fontsize = 16)

##positivos
axs[2,2].bar(ALT.index, ALT['impoC50'], color='#FF9B9B', width =1)
axs[2,2].bar(ALT.index, ALT['impoN50'], bottom=ALT['impoC50'], color='#ADA4BA', width =1)
axs[2,2].bar(ALT.index, ALT['impoO50'], bottom=ALT['impoC50']+ALT['impoN50'], color='#BCEE9B', width =1)
axs[2,2].bar(ALT.index, ALT['impoS50'], bottom=ALT['impoC50']+ALT['impoN50']+ALT['impoO50'], color='#D7B99B', width =1)
axs[2,2].set_ylim(0, 700)
axs[2,2].set_xticks(range(0, len(ALT.index), 2))
axs[2,2].set_xticklabels(ALT.index[::2])
axs[2,2].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[2,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,2].tick_params(axis='both', labelsize=0, color='white')
axs[2,2].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(-1.3, -1.8), loc='center left', borderaxespad=0.,fontsize=10, ncols=4)
axs[2,2].set_xlim(-0.5, 23.5)

# ~ axs[0,2].set_xlim(-0.5, 23.5)


#################### ALT-GD ###############################
################### 2030
##positivos
cols = ['impoC30', 'impoN30', 'impoO30', 'impoS30']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[3,0].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[3,0].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

axs[3,0].set_ylim(-300, 300)
axs[3,0].set_xticks(range(0, len(numeric_labels), 2))
# ~ axs[3,0].set_xticklabels(RESTA1.index[::2])
axs[3,0].set_xticklabels(numeric_labels[::2])


axs[3,0].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[3,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[3,0].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[3,0].set_xlim(-0.5, 23.5)
axs[3,0].yaxis.set_tick_params(labelsize=10)

################### 2040
##positivos
cols = ['impoC40', 'impoN40', 'impoO40', 'impoS40']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[3,1].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[3,1].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

# ~ axs[3,1].set_ylim(-350, 350)
axs[3,1].set_xticks(range(0, len(RESTA1.index), 2))
# ~ axs[3,1].set_xticklabels(RESTA1.index[::2])
axs[3,1].set_xticklabels(numeric_labels[::2])

axs[3,1].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[3,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[3,1].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[3,1].yaxis.set_tick_params(labelsize=0, color='white')

axs[3,1].set_xlim(-0.5, 23.5)


################### 2050
##positivos

cols = ['impoC50', 'impoN50', 'impoO50', 'impoS50']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[3,2].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[3,2].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

# ~ axs[3,2].set_ylim(-350, 350)
axs[3,2].set_xticks(range(0, len(RESTA1.index), 2))
# ~ axs[3,2].set_xticklabels(RESTA1.index[::2])
axs[3,2].set_xticklabels(numeric_labels[::2])


axs[3,2].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[3,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[3,2].xaxis.set_tick_params(labelsize=10, rotation=90)
axs[3,2].yaxis.set_tick_params(labelsize=0, color='white')
axs[3,2].set_xlim(-0.5, 23.5)

#################### EXPORTS ###############################

ALT = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosTEN.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
ALTGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosTENGD.txt', header=0, delimiter=';', na_values='-999',index_col='hora')


RESTA1 = ALTGD-ALT
print(RESTA1)

#################### ALT ###############################
################### 2030
##positivos
axs[0,0].set_title('2030', fontsize = 12)
axs[0,0].bar(ALT.index, ALT['expoC30'], color='#FF9B9B', width =1)
axs[0,0].bar(ALT.index, ALT['expoN30'], bottom=ALT['expoC30'], color='#ADA4BA', width =1)
axs[0,0].bar(ALT.index, ALT['expoO30'], bottom=ALT['expoC30']+ALT['expoN30'], color='#BCEE9B', width =1)
axs[0,0].bar(ALT.index, ALT['expoS30'], bottom=ALT['expoC30']+ALT['expoN30']+ALT['expoO30'], color='#D7B99B', width =1)
axs[0,0].set_ylim(0, 700)
axs[0,0].set_xticks(range(0, len(ALT.index), 2))
axs[0,0].set_xticklabels(ALT.index[::2])
axs[0,0].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[0,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,0].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[0,0].yaxis.set_tick_params(labelsize=10)
axs[0,0].set_xlim(-0.5, 23.5)
axs[0,0].text(1, 50, 'dry season', fontsize=9)
axs[0,0].text(12, 50, 'humid season', fontsize=9)

################### 2040
axs[0,1].set_title('Exports \n 2040', fontsize = 12)
##positivos
axs[0,1].bar(ALT.index, ALT['expoC40'], color='#FF9B9B', width =1)
axs[0,1].bar(ALT.index, ALT['expoN40'], bottom=ALT['expoC40'], color='#ADA4BA', width =1)
axs[0,1].bar(ALT.index, ALT['expoO40'], bottom=ALT['expoC40']+ALT['expoN40'], color='#BCEE9B', width =1)
axs[0,1].bar(ALT.index, ALT['expoS40'], bottom=ALT['expoC40']+ALT['expoN40']+ALT['expoO40'], color='#D7B99B', width =1)
axs[0,1].set_ylim(0, 700)
axs[0,1].set_xticks(range(0, len(ALT.index), 2))
axs[0,1].set_xticklabels(ALT.index[::2])
axs[0,1].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[0,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,1].tick_params(axis='both', labelsize=0, color='white')
axs[0,1].set_xlim(-0.5, 23.5)
axs[0,1].text(1, 50, 'dry season', fontsize=9)
axs[0,1].text(12, 50, 'humid season', fontsize=9)

################### 2050

##positivos
axs[0,2].set_title('2050', fontsize = 12)

axs[0,2].bar(ALT.index, ALT['expoC50'], color='#FF9B9B', width =1)
axs[0,2].bar(ALT.index, ALT['expoN50'], bottom=ALT['expoC50'], color='#ADA4BA', width =1)
axs[0,2].bar(ALT.index, ALT['expoO50'], bottom=ALT['expoC50']+ALT['expoN50'], color='#BCEE9B', width =1)
axs[0,2].bar(ALT.index, ALT['expoS50'], bottom=ALT['expoC50']+ALT['expoN50']+ALT['expoO50'], color='#D7B99B', width =1)
axs[0,2].set_ylim(0, 700)
axs[0,2].set_xticks(range(0, len(ALT.index), 2))
axs[0,2].set_xticklabels(ALT.index[::2])
axs[0,2].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[0,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,2].tick_params(axis='both', labelsize=0, color='white')
# ~ axs[0,2].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.1, 0.6), loc='center left', borderaxespad=0.,fontsize=12)
axs[0,2].text(1, 50, 'dry season', fontsize=9)
axs[0,2].text(12, 50, 'humid season', fontsize=9)
axs[0,2].set_xlim(-0.5, 23.5)


#################### ALT-GD ###############################
################### 2030
##positivos
cols = ['expoC30', 'expoN30', 'expoO30', 'expoS30']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,0].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,0].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

axs[1,0].set_ylim(-300, 300)
axs[1,0].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,0].set_xticklabels(RESTA1.index[::2])
axs[1,0].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,0].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[1,0].set_xlim(-0.5, 23.5)
axs[1,0].yaxis.set_tick_params(labelsize=10)

################### 2040
##positivos
cols = ['expoC40', 'expoN40', 'expoO40', 'expoS40']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,1].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,1].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

# ~ axs[1,1].set_ylim(-350, 350)
axs[1,1].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,1].set_xticklabels(RESTA1.index[::2])
axs[1,1].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,1].tick_params(axis='both', labelsize=0, color='white')
axs[1,1].set_xlim(-0.5, 23.5)


################### 2050
##positivos

cols = ['expoC50', 'expoN50', 'expoO50', 'expoS50']
colors = ['#FF9B9B', '#ADA4BA', '#BCEE9B', '#D7B99B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,2].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, width =1)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,2].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, width =1)
    neg_bottoms += neg_data[col].values

# ~ axs[1,2].set_ylim(-350, 350)
axs[1,2].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,2].set_xticklabels(RESTA1.index[::2])
# ~ axs[1,2].set_xticklabels(labels)
axs[1,2].axvline(x=11.5, color='black', linewidth=1, label='_nolegend_')
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,2].tick_params(axis='both', labelsize=0, color='white')
axs[1,2].set_xlim(-0.5, 23.5)

fig.subplots_adjust(wspace=0.05, hspace=0.1)
shift = 0.05
for ax in axs[2:, :].flat:  # rows 3 onward, all columns
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0 - shift, pos.width, pos.height])

fig.text(0.91, 0.79, 'ALT', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.91, 0.6, '(ALT-SD) \n  - ALT', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.91, 0.4, 'ALT', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.91, 0.2, '(ALT-SD) \n  - ALT', va='center' ,fontsize=12, rotation='vertical')  
fig.text(0.04, 0.5, '[MW]', va='center' ,fontsize=12, rotation='vertical')  

plt.savefig('tradeALT.svg', dpi=300, bbox_inches="tight")
