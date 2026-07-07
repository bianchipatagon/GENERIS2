import matplotlib.pyplot as plt
#59901kbep
cat1 = 'NG','LPG','Diesel','Gasoline','Elec.','Biomass'
counts1 = [ 14685,3619 ,15016,  12959 , 6240, 5441]
colors1 = ['silver','dimgrey', 'black','saddlebrown','goldenrod','#207653']
# ~ hatch1 = ['', '/', '', '.', '/', '', '']

#6240kbep
cat2 = 'Norte', 'Centro', 'Oriente', 'Sur', 'Pando'
counts2 = [  1340, 1327, 2463 ,1069, 37 ]
colors2 = ['#FBAA1B','#8FC73E', '#207653','#A1140B','#36495A']

cat3 = 'Residential', 'Transport', 'Industry', 'Commercial & Public', 'Agriculture, Fishing & Mining', 'Construction'
counts3 = [   2387 ,17 ,1497 ,1447 ,697 ,195]
colors3 = ['#36495A','#207653', '#FBAA1B','#8FC73E','#A1140B', '#6D6F70']


fig,(ax1, ax2, ax3) = plt.subplots(1,3,figsize=(7,7), sharey=True)
# ~ gs = fig.add_gridspec(2, 2, wspace=0.1, hspace=0.3)

# ~ ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title('Source', fontsize=16, fontweight='bold')
ax1.pie(counts1, labels = cat1, autopct='%1.1f%%',colors=colors1,wedgeprops=dict(width=0.98, edgecolor='white'))
ax1.legend(cat1,  loc="lower center", bbox_to_anchor=(0.5, -0.9, 0.5, 1), fontsize=13, frameon=False)

# ~ ax.pie(sizes. labels=labels. autopct='%1.1f%%')
# ~ ax.set_title('% generación Suiza 2023'. fontsize = 16)
# ~ ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title('Region', fontsize=16, fontweight='bold')
ax2.pie(counts2, labels = cat2, autopct='%1.1f%%',colors=colors2,wedgeprops=dict(width=0.98, edgecolor='white'))
ax2.legend(cat2,  loc="lower center", bbox_to_anchor=(0.4, -0.8, 0.5, 1), fontsize=13, frameon=False)

# ~ ax3 = fig.add_subplot(gs[1, :])

ax3.set_title('Sector', fontsize=16, fontweight='bold')
ax3.pie(counts3, labels = cat3, autopct='%1.1f%%',colors=colors3,wedgeprops=dict(width=0.98, edgecolor='white'))
ax3.legend(cat3,  loc="lower center", bbox_to_anchor=(0.75, -0.9, 0.5, 1), fontsize=13, frameon=False)


fig.subplots_adjust(wspace=0.05)

plt.savefig('demanda.svg',dpi=300, bbox_inches="tight")
