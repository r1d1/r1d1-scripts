#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

for i in np.arange(10):
	field = np.random.uniform(-2 * np.pi, 2 * np.pi, [10,10])

	amplitude = np.random.rand()
	U = amplitude * np.cos(field)
	V = amplitude * np.sin(field)
	X, Y = np.meshgrid(np.arange(10), np.arange(10))

	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.quiver(X, Y, U, V)

plt.show()
