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

tmp=zip(*playTimes)
timesPlayed=tmp[1]

#print timesPlayed
timesData = open(timeDataFile, 'w')
timesData.write('# time\n')
for timeline in timesPlayed:
	timesData.write(timeline+'\n')
timesData.close()
