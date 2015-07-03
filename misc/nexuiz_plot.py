#!/usr/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dataFile = 'processed_time_nex.txt'

#dataToPlot=open(dataFile)
#timeValuesStr = dataToPlot.read()
#dataToPlot.close()

# MAtplotlib general parameters :
params = {
	'axes.labelsize': 8,
	'text.fontsize': 8,
	'legend.fontsize': 10,
	'xtick.labelsize': 10,
	'ytick.labelsize': 10,
	'text.usetex': False,
	'figure.figsize': [6.0, 6.0]
}
mpl.rcParams.update(params)


timeValues = np.loadtxt(dataFile)

print 'Games played:',len(timeValues)

x = np.arange(len(timeValues))
xTicksLabels=['Game '+str(n) for n in np.arange(len(timeValues))]
fig, ax1 = plt.subplots()
ax2=plt.twinx()

#plt.axes(frameon=0)
#plt.grid()

#plt.plot(x, timeValues /60.0, linewidth=2, color='b')
#plt.plot(x, np.cumsum(timeValues/60.0), linewidth=2, color='r')
plt.xticks(np.arange(len(timeValues)), xTicksLabels, rotation='vertical')
ax1.plot(x, timeValues /60.0, linewidth=2, color='b')
ax2.plot(x, np.cumsum(timeValues/60.0), linewidth=2, color='r')
ax1.set_xlabel('Games played')
ax1.set_xlabel('Games played')
ax1.set_ylabel('Time (min)', color='b')
ax2.set_ylabel('Cumulative time', color='r')
#plt.ylabel('Time (min)', color='b')
#plt.set_ylabel('Cumulative time', color='r')
leg = plt.legend(["Game duration", "Total time"], loc=2)
#leg1 = plt.legend(["Game duration"], loc=2)
#leg2 = plt.legend(["Total time"], loc=1)

#frame=leg.get_frame()
#frame.set_facecolor('0.9')
#frame.set_edgecolor('0.9')
#frame1=leg1.get_frame()
#frame2=leg2.get_frame()
#frame1.set_facecolor('0.9')
#frame1.set_edgecolor('0.9')
#frame2.set_facecolor('0.9')
#frame2.set_edgecolor('0.9')

plt.show()

#fig.savefig('durationsNexuiz.png')
