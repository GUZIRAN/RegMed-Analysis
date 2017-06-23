import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as ssn

datafile = 'data.txt'     # put the file location here
savefile = 'heatmap.png'  # where the heatmap should be saved.

data = pd.read_table(datafile)
header = list(data.columns)

for i in xrange(len(header)):
	header[i] = header[i].split('.',1)[0]

gene = list(set(header))
DataList = []
smax = np.nanmax(data.values.astype(np.float64))
smin = np.nanmin(data.values.astype(np.float64))


for i in xrange(len(gene)):
	DataList.append(data.ix[:,[x==gene[i] for x in header]])

pnum=len(gene)
fig, axn = plt.subplots(1, pnum, sharex = False)
cbar_ax = fig.add_axes([.91, .3, .03, .4])
fig.set_size_inches(18.5, 10.5)

for i, ax in enumerate(axn.flat):
	ax.set_title(gene[i])
	ssn.heatmap(DataList[i], ax = ax, cmap="YlGnBu", cbar_ax = None if i else cbar_ax, cbar = (i == 0), xticklabels = False, yticklabels = False,  vmin = smin,vmax = smax)
plt.savefig(savefile,dpi=300)
plt.show()
