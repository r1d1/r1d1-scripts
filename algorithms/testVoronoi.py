#!/usr/bin/python

# TDD of Voronoi tesselation algorithm

import matplotlib.pyplot as plt
import numpy as np

from Voronoi import Voronoi

sizeEnv = (100,100)

np.set_printoptions(linewidth=200)

# Build map of environment, 0 is free space, 1 is obstacle :
mapEnv = np.zeros(sizeEnv)
for x in np.arange(sizeEnv[0]):
	if (x > 15) and (x < 50):
		for y in np.arange(sizeEnv[1]):
			if (x > y) and (y < 40):
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

#--------------------------------------------------------
# Construct Voronoi tesselator :
tesseling = Voronoi()
print tesseling.centerList

# Add center by hand for TDD :
tesseling.addCenter(5, 5)
tesseling.addCenter(50.0, 35)
tesseling.addCenter(75, 20)
print tesseling.centerList
tesseling.senseLasers(mapEnv)
#tesseling.updateFrontiers()

#--------------------------------------------------------
# Display centers, frontiers, maps :
xd=(zip(*tesseling.centerList))[0]
yd=(zip(*tesseling.centerList))[1]
xa=tesseling.position[0]
ya=tesseling.position[1]

plt.plot(xd, yd, 'o', color='r', ms=10)
plt.plot(xa, ya, 'd', color='b', ms=15)
mapplot=plt.imshow(mapEnv, interpolation='none', origin='upper')
mapplot.set_cmap('Greys')
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([0.0, 100.0])
plt.ylim([0.0, 100.0])
plt.show()

