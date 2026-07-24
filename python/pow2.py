import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

pow30 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen30.txt', header=0, delimiter=',', na_values='-999')
pow40 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen40.txt', header=0, delimiter=',', na_values='-999')
pow50 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen50.txt', header=0, delimiter=',', na_values='-999')

alt30 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/AltGen30.txt', header=0, delimiter=',', na_values='-999')
alt40 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/AltGen40.txt', header=0, delimiter=',', na_values='-999')
alt50 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/AltGen50.txt', header=0, delimiter=',', na_values='-999')

tdry30 = pow30.iloc[0:12]
twet30 = pow30.iloc[12:24]

tdry40 = pow40.iloc[0:12]
twet40 = pow40.iloc[12:24]

tdry50 = pow50.iloc[0:12]
twet50 = pow50.iloc[12:24]

adry30 = alt30.iloc[0:12]
awet30 = alt30.iloc[12:24]

adry40 = alt40.iloc[0:12]
awet40 = alt40.iloc[12:24]

adry50 = alt50.iloc[0:12]
awet50 = alt50.iloc[12:24]

fig, axs = plt.subplots(3,4,figsize=(12,4),sharex=True, sharey=True)

#################### TENDENCIAL ###############################
################### 2030
##positivos
axs[0,0].bar(tdry30['hora'], tdry30['Solar'], color='#FBAA1B')
axs[0,0].bar(tdry30['hora'], tdry30['Eolica'], bottom=tdry30['Solar'], color='#8FC73E')
axs[0,0].bar(tdry30['hora'], tdry30['Hidro'], bottom=tdry30['Solar']+tdry30['Eolica'], color='#0000CD')
axs[0,0].axhline(linewidth=1, color='black')

##negativos
axs[0,0].bar(tdry30['hora'], tdry30['Fosiln'], color='black')
axs[0,0].bar(tdry30['hora'], tdry30['Solarn'], bottom=tdry30['Fosiln'], color='#FBAA1B')
axs[0,0].bar(tdry30['hora'], tdry30['Eolican'],bottom= tdry30['Fosiln']+tdry30['Solarn'], color='#8FC73E')
axs[0,0].bar(tdry30['hora'], tdry30['Hidron'], bottom=tdry30['Fosiln']+tdry30['Solarn']+tdry30['Eolican'], color='#0000CD')
axs[0,0].set_ylim(-750, 0)
axs[0,0].set_title('Dry season', fontsize = 16)
axs[0,0].yaxis.set_tick_params(labelsize=12)
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,0].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')


##positivos
axs[0,1].bar(twet30['hora'], twet30['Fosil'], color='black')
axs[0,1].bar(twet30['hora'], twet30['Solar'], bottom=twet30['Fosil'], color='#FBAA1B')
axs[0,1].bar(twet30['hora'], twet30['Eolica'], bottom=twet30['Fosil']+twet30['Solar'], color='#8FC73E')
axs[0,1].bar(twet30['hora'], twet30['Hidro'], bottom=twet30['Fosil']+twet30['Solar']+twet30['Eolica'], color='#0000CD')
axs[0,1].axhline(linewidth=1, color='black')

##negativos
axs[0,1].bar(twet30['hora'], twet30['Fosiln'], color='black')
axs[0,1].bar(twet30['hora'], twet30['Solarn'], bottom=twet30['Fosiln'], color='#FBAA1B')
axs[0,1].bar(twet30['hora'], twet30['Eolican'], bottom=twet30['Fosiln']+twet30['Solarn'], color='#8FC73E')
axs[0,1].bar(twet30['hora'], twet30['Hidron'], bottom=twet30['Fosiln']+twet30['Solarn']+twet30['Eolican'], color='#0000CD')

axs[0,1].set_title('Humid season', fontsize = 16)
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,1].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[0,1].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

# ~ ax2.legend(["TG", "TV", "Motor", "CC", "Solar", "Eolica", "Hidro"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

################### 2040

##positivos
axs[1,0].bar(tdry40['hora'], tdry40['Fosil'], color='black')
axs[1,0].bar(tdry40['hora'], tdry40['Solar'], bottom=tdry30['Fosil'], color='#FBAA1B')
axs[1,0].bar(tdry40['hora'], tdry40['Eolica'], bottom=tdry30['Fosil']+tdry40['Solar'], color='#8FC73E')
axs[1,0].axhline(linewidth=1, color='black')

##negativos
axs[1,0].bar(tdry40['hora'], tdry40['Fosiln'], color='black')
axs[1,0].bar(tdry40['hora'], tdry40['Hidron'], bottom=tdry40['Fosiln'], color='#0000CD')
# ~ axs[1,0].set_ylim(-650, 200)
# ~ axs[1,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[1,0].yaxis.set_tick_params(labelsize=12)
axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].set_ylabel('[MW]', fontsize=14)
axs[1,0].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')

##negativos
axs[1,1].bar(twet40['hora'], twet40['Fosiln'], color='black')
axs[1,1].bar(twet40['hora'], twet40['Solarn'], bottom= twet40['Fosiln'], color='#FBAA1B')
axs[1,1].bar(twet40['hora'], twet40['Eolican'], bottom= twet40['Fosiln']+twet40['Solarn'], color='#8FC73E')
axs[1,1].bar(twet40['hora'], twet40['Hidron'], bottom= twet40['Fosiln']+twet40['Solarn']+twet40['Eolican'], color='#0000CD')

##positivos
axs[1,1].bar(twet40['hora'], twet40['Fosil'], color='black')
axs[1,1].bar(twet40['hora'], twet40['Solar'], bottom=twet40['Fosil'], color='#FBAA1B')
axs[1,1].bar(twet40['hora'], twet40['Eolica'], bottom=twet40['Fosil']+twet40['Solar'], color='#8FC73E')
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')

# ~ axs[1,1].set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[1,1].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

################### 2050

##negativos
axs[2,0].bar(tdry50['hora'], tdry50['Fosiln'], color='black')
axs[2,0].bar(tdry50['hora'], tdry50['Hidron'], bottom=tdry50['Fosiln'], color='#0000CD')
# ~ axs[2,0].set_ylim(-650, 200)
# ~ axs[2,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[2,0].yaxis.set_tick_params(labelsize=12)
axs[2,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,0].axhline(linewidth=1, color='black')
##negativos
axs[2,0].bar(tdry50['hora'], tdry50['Fosil'], color='black')

##positivos
axs[2,1].bar(twet50['hora'], twet50['Fosiln'], color='black')
axs[2,1].bar(twet50['hora'], twet50['Hidron'], bottom=twet50['Fosiln'], color='#0000CD')
# ~ axs[2,1].set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
axs[2,1].xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ axs[2,1].legend(["TG", "TV", "Motor", "CC", "Solar"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
axs[2,1].axhline(linewidth=1, color='black')

##negativos
axs[2,1].bar(twet50['hora'], twet50['Fosil'], color='black')
axs[2,1].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

#################### ALTERNATIVO ###############################

################### 2030
##positivos
axs[0,2].bar(adry30['hora'], adry30['Fosil'], color='black', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Solar'], bottom=adry30['Fosil'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Eolica'], bottom=adry30['Fosil']+adry30['Solar'], color='#8FC73E', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Hidro'], bottom=adry30['Fosil']+adry30['Solar']+adry30['Eolica'], color='#0000CD', alpha=0.8)
axs[0,2].axhline(linewidth=1, color='black')

##negativos
axs[0,2].bar(adry30['hora'], adry30['Fosiln'], color='black', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Solarn'], bottom=adry30['Fosiln'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Eolican'], bottom=adry30['Fosiln']+adry30['Solarn'], color='#8FC73E', alpha=0.8)
axs[0,2].bar(adry30['hora'], adry30['Hidron'], bottom=adry30['Fosiln']+adry30['Solarn']+adry30['Eolican'], color='#0000CD', alpha=0.8)
# ~ axs[0,2].set_ylim(-650, 200)
axs[0,2].set_title('Dry season', fontsize = 16)
axs[0,2].yaxis.set_tick_params(labelsize=12)
axs[0,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,2].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[0,2].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')
##positivos
axs[0,3].bar(awet30['hora'], awet30['Fosil'], color='black', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Solar'], bottom=awet30['Fosil'], color='#FBAA1B', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Eolica'], bottom=awet30['Fosil']+awet30['Solar'], color='#8FC73E', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Hidro'], bottom=awet30['Fosil']+awet30['Solar']+awet30['Eolica'], color='#0000CD', alpha=0.8)
axs[0,3].axhline(linewidth=1, color='black')

##negativos
axs[0,3].bar(awet30['hora'], awet30['Fosiln'], color='black', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Solarn'], bottom=awet30['Fosiln'], color='#FBAA1B', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Eolican'], bottom=awet30['Fosiln']+awet30['Solarn'], color='#8FC73E', alpha=0.8)
axs[0,3].bar(awet30['hora'], awet30['Hidron'], bottom=awet30['Fosiln']+awet30['Solarn']+awet30['Eolican'], color='#0000CD', alpha=0.8)

axs[0,3].set_title('Humid season', fontsize = 16)
axs[0,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,3].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[0,3].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')
# ~ axs[0.3].legend(["Fosil", "Solar","Eólica","Hidro"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

################### 2040

##positivos
axs[1,2].bar(adry40['hora'], adry40['Fosil'], color='black', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Solar'], bottom=adry30['Fosil'], color='#FBAA1B', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Eolica'], bottom=adry30['Fosil']+adry40['Solar'], color='#8FC73E', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Hidro'], bottom=adry30['Fosil']+adry40['Solar']+adry40['Eolica'], color='#0000CD', alpha=0.8)
axs[1,2].axhline(linewidth=1, color='black')

##negativos
axs[1,2].bar(adry40['hora'], adry40['Fosiln'], color='black', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Solarn'], bottom=adry40['Fosiln'], color='#FBAA1B', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Eolican'], bottom=adry40['Fosiln']+adry40['Solarn'], color='#8FC73E', alpha=0.8)
axs[1,2].bar(adry40['hora'], adry40['Hidron'], bottom=adry40['Fosiln']+adry40['Solarn']+adry40['Eolican'], color='#0000CD', alpha=0.8)
# ~ axs[1,2].set_ylim(-650, 200)
# ~ axs[1,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[1,2].yaxis.set_tick_params(labelsize=12)
axs[1,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,2].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[1,2].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

##negativos
axs[1,3].bar(awet40['hora'], awet40['Fosiln'], color='black', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Solarn'], bottom= awet40['Fosiln'], color='#FBAA1B', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Eolican'], bottom= awet40['Fosiln']+awet40['Solarn'], color='#8FC73E', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Hidron'], bottom= awet40['Fosiln']+awet40['Solarn']+awet40['Eolican'], color='#0000CD', alpha=0.8)

##positivos
axs[1,3].bar(awet40['hora'], awet40['Fosil'], color='black', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Solar'], bottom=awet40['Fosil'], color='#FBAA1B', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Eolica'], bottom=awet40['Fosil']+awet40['Solar'], color='#8FC73E', alpha=0.8)
axs[1,3].bar(awet40['hora'], awet40['Hidro'], bottom= awet40['Fosil']+awet40['Solar']+awet40['Eolica'], color='#0000CD', alpha=0.8)
axs[1,3].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,3].legend(["Fossil", "Solar","Wind","Hydro"], frameon=False,bbox_to_anchor=(-2.2, -1.8), loc='upper left', borderaxespad=0.,fontsize=14, ncols=4)
axs[1,3].xaxis.set_tick_params(labelsize=0, rotation=90,color='white')
axs[1,3].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

################### 2050

##positivos
axs[2,2].bar(adry50['hora'], adry50['Fosil'], color='black', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Solar'], bottom=adry50['Fosil'], color='#FBAA1B', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Eolica'], bottom=adry50['Fosil']+adry50['Solar'], color='#8FC73E', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Hidro'], bottom=adry50['Fosil']+adry50['Solar']+adry50['Eolica'], color='#0000CD', alpha=0.8)
axs[2,2].axhline(linewidth=1, color='black')

##negativos
axs[2,2].bar(adry50['hora'], adry50['Fosiln'], color='black', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Solarn'], bottom=adry50['Fosiln'], color='#FBAA1B', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Eolican'], bottom=adry50['Fosiln']+adry50['Solarn'], color='#8FC73E', alpha=0.8)
axs[2,2].bar(adry50['hora'], adry50['Hidron'], bottom=adry50['Fosiln']+adry50['Solarn']+adry50['Eolican'], color='#0000CD', alpha=0.8)
# ~ axs[2,2].set_ylim(-650, 200)
# ~ axs[1,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[2,2].yaxis.set_tick_params(labelsize=12)
axs[2,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,2].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

##positivos
axs[2,3].bar(awet50['hora'], awet50['Fosil'], color='black')
axs[2,3].bar(adry50['hora'], awet50['Solar'], bottom=adry30['Fosil'], color='#FBAA1B')
axs[2,3].bar(awet50['hora'], awet50['Eolica'], bottom=awet30['Fosil']+awet50['Solar'], color='#8FC73E')
axs[2,3].bar(awet50['hora'], awet50['Hidro'], bottom=awet30['Fosil']+awet50['Solar']+awet50['Eolica'], color='#0000CD')
axs[2,3].axhline(linewidth=1, color='black')

##negativos
axs[2,3].bar(awet50['hora'], awet50['Fosiln'], color='black')
axs[2,3].bar(awet50['hora'], awet50['Solarn'], bottom=awet30['Fosiln'], color='#FBAA1B')
axs[2,3].bar(awet50['hora'], awet50['Eolican'], bottom=awet30['Fosiln']+awet50['Solarn'], color='#8FC73E')
axs[2,3].bar(awet50['hora'], awet50['Hidron'], bottom=awet30['Fosiln']+awet50['Solarn']+awet50['Eolican'], color='#0000CD')
# ~ axs[2,3].set_ylim(-650, 200)
# ~ axs[1,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[2,3].yaxis.set_tick_params(labelsize=12)
axs[2,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,3].yaxis.set_tick_params(labelsize=0, rotation=90,color='white')

fig.subplots_adjust(wspace=0.05, hspace=0.05)
fig.text(0.91, 0.75, '2030', va='center' ,fontsize=14, rotation='vertical')  
fig.text(0.91, 0.5, '2040', va='center' ,fontsize=14, rotation='vertical')  
fig.text(0.91, 0.25, '2050', va='center' ,fontsize=14, rotation='vertical')  
# ~ fig.text(0.5, 0.005, 'hours', va='center' ,fontsize=14)  

# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
fig.text(.26, 0.97, '(BAU-DS) - BAU', va='center' ,fontsize=16)  
fig.text(.66, 0.97, '(ALT-DS) - ALT', va='center' ,fontsize=16)  

plt.savefig('Pow2.png', dpi=300, bbox_inches="tight")
