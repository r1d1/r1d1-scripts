#!/usr/bin/python

import sys
import os
import time
import matplotlib.pyplot as plt
import pylab as plb
import numpy as np
import json
import math
import re

rawLogFile='time_nex.txt'
timeDataFile='processed_time_nex.txt'

rawdata = open(rawLogFile)
text= rawdata.read()
rawdata.close()

print type(text)
playTimes=re.findall('(real )([0-9]{1,5}\.[0-9]{0,2})', text)
# Extract date :
playDates=re.findall('(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\s([1-3]{,1}[0-9])\s(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre)\s([0-9]{4}),\s([0-9]{1,2}:[0-9]{2}:[0-9]{2})\s', text)

# reverse tuple :
#playDates[0] = playDates[0][::-1]
print playDates
print len(playDates), len(playTimes)
tmp=zip(*playTimes)
timesPlayed=tmp[1]

#print timesPlayed
timesData = open(timeDataFile, 'w')
timesData.write('# time\n')
for timeline in timesPlayed:
	timesData.write(timeline+'\n')
timesData.close()
