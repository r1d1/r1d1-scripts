#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

dataFile = 'processed_time_nex.txt'

#dataToPlot=open(dataFile)
#timeValuesStr = dataToPlot.read()
#dataToPlot.close()

timeValues = np.loadtxt(dataFile)

print 'Games played:',len(timeValues)

x = np.arange(len(timeValues))
fig, ax1 = plt.subplots()
ax2=plt.twinx()

ax1.plot(x, timeValues /60.0, 'b')
ax2.plot(x, np.cumsum(timeValues/60.0), 'r')
ax1.set_xlabel('Games played')
ax1.set_ylabel('Time (min)', color='b')
ax2.set_ylabel('Cumulative time', color='r')


plt.show()
