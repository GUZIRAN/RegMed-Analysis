import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as ssn


from pyheatmap.heatmap import HeatMap
data = pd.read_csv('Data.csv')
header = list(data.columns)

for i in xrange(len(header)):
	header[i] = header[i].split('.',1)[0]
#print header
ct = {x:header.count(x) for x in header}
gene = ct.keys()
Tdata = data.T
Tdata['Gene'] = header
DataList = []

for i in xrange(len(gene)):
	DataList.append(Tdata.loc[Tdata.Gene == gene[i]])

for i in xrange(len(gene)):
	DataList[i]=DataList[i].drop('Gene',1).T
	DataList[i].index = range(len(DataList[i]))
	print gene[i] + 'file shape :' + str (DataList[i].shape)
	


#plt.pcolor(DataList[0])
#plt.yticks(np.arange(0.5, len(DataList[0].index), 1), DataList[0].index)
#plt.xticks(np.arange(0.5, len(DataList[0].columns), 1), DataList[0].columns)
d1=DataList[0]
d1h=HeatMap(d1)


