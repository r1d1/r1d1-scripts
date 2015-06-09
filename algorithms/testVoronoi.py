#!/usr/bin/python

# TDD of Voronoi tesselation algorithm

import matplotlib.pyplot as plt
import numpy as np
import time

from Voronoi import Voronoi

sizeEnv = (100,100)

np.set_printoptions(linewidth=200)

# Build map of environment, 0 is free space, 1 is obstacle :
mapEnv = np.zeros(sizeEnv)
for x in np.arange(sizeEnv[0]):
	if (x > 15) and (x < 50):
		for y in np.arange(sizeEnv[1]):
			if (x > y) and (y < 30):
				mapEnv[y,x] = 1

for x in np.arange(sizeEnv[0]):
	if (x < 20) or (x > 75):
		for y in np.arange(sizeEnv[1]):
			if (x < y) and (y > 80):
				mapEnv[y,x] = 1

for x in np.arange(sizeEnv[0]):
	if (x > 40) and (x < 70):
		for y in np.arange(sizeEnv[1]):
			if (y > 50):
				mapEnv[y,x] = 1

#for x in np.arange(sizeEnv[0]):
#	if (x > 50) and (x < 70):
#		for y in np.arange(sizeEnv[1]):
#			if (y > 30) and (y < 70):
#				mapEnv[y,x] = 1

#for x in np.arange(sizeEnv[0]):
#	if (x > 20) and (x < 40):
#		for y in np.arange(sizeEnv[1]):
#			if (y > 20) and (y < 45):
#				mapEnv[y,x] = 1

mapEnv = mapEnv.T
#--------------------------------------------------------
# Construct Voronoi tesselator :
tesseling = Voronoi()
print tesseling.centerList

# Add center by hand for TDD :
#tesseling.addCenter(5, 5)
#tesseling.addCenter(10.0, 90.0)
#tesseling.addCenter(90.0, 10.0)
#tesseling.addCenter(10.0, 10.0)
#tesseling.addCenter(90.0, 90.0)
print "Center list:",tesseling.centerList
tesseling.senseLasers(mapEnv)
#print "##### Sense:", tesseling.leftDist, tesseling.rightDist, tesseling.topDist, tesseling.downDist, tesseling.sensors
print "##### Sense:", tesseling.sensors

print "Initial position"
print "Distances to active center:",tesseling.distToActiveCenter()
print tesseling.computeDistToCenters()
print "update active center :"
tesseling.updateActiveCenter()
print "Distances:",tesseling.distToActiveCenter()
print tesseling.computeDistToCenters()

print "##### Move ---------"
tesseling.moveTo(75, 33)
print "New position", tesseling.position
print "Active center", tesseling.activeCenter
print "Distances to active center:",tesseling.distToActiveCenter()
print tesseling.computeDistToCenters()
print "update active center :"
tesseling.updateActiveCenter()
print "Active center", tesseling.activeCenter
print "Distances to active center:",tesseling.distToActiveCenter()
tesseling.senseLasers(mapEnv)
print "##### Sense:", tesseling.sensors

print "##### Move ---------"
tesseling.moveTo(45, 35)
print "New position", tesseling.position
print "Active center", tesseling.activeCenter
print "Distances to active center:",tesseling.distToActiveCenter()
print tesseling.computeDistToCenters()
print "update active center :"
tesseling.updateActiveCenter()
print "Active center", tesseling.activeCenter
print "Distances to active center:",tesseling.distToActiveCenter()
tesseling.senseLasers(mapEnv)
print "##### Sense:", tesseling.sensors

plt.ion()
xd=(zip(*tesseling.centerList))[0]
yd=(zip(*tesseling.centerList))[1]
cl, = plt.plot(yd, xd, 'o', color='r', ms=10)
mapplot=plt.imshow(mapEnv, interpolation='none')
mapplot.set_cmap('Greys')
plt.xlabel("y")
plt.ylabel("x")
plt.xlim([0.0, 100.0])
plt.ylim([0.0, 100.0])
plt.colorbar()
plt.show()
print "##### Drive --------"
previousLen = len(tesseling.centerList)
for ts in np.arange(2000):
	tesseling.forwardDrive(mapEnv)
	#print "New position", tesseling.position
#--------------------------------------------------------
# Display centers, frontiers, maps :
	#print "Display -------------------"
	if len(tesseling.centerList) > previousLen:
		xd=(zip(*tesseling.centerList))[0]
		yd=(zip(*tesseling.centerList))[1]
		cl.remove()
		#print "coordinates:", xd, yd, xa, ya
		cl, = plt.plot(yd, xd, 'o', color='r', ms=10)
	
	xa=tesseling.position[0]
	ya=tesseling.position[1]
	ln, = plt.plot(ya, xa, 's', color='b')
	#plt.show()
	plt.draw()
	time.sleep(0.01)
	ln.remove()

plt.waitforbuttonpress()
