#!/usr/bin/python

import math
import numpy as np

nbLaserDir = 8 # This must not change
maxLaserRange = 10

class Voronoi:
	def __init__(self):
		self.centerList=[]
		self.edgeList=[]
		self.position=(15, 15)
		self.laserMeasurement=np.zeros(nbLaserDir).tolist()
		print "Ctor"

	# Voronoi
	def addCenter(self, x, y):
		self.centerList.append((x, y))
	
	def updateFrontiers(self, method="fortune"):
		print "Method:",method
		# Implementation
	
	# Agent
	def senseLasers(self, envmap):
		# local estimation :
		localMap = np.ones((2*maxLaserRange+1, 2*maxLaserRange+1))
		print localMap
		# measurement :
		print envmap.shape
		minx=self.position[0]-maxLaserRange if (self.position[0]-maxLaserRange) > 0 else 0
		maxx=self.position[0]+maxLaserRange if (self.position[0]+maxLaserRange) < envmap.shape[0] else envmap.size[0]
		miny=self.position[1]-maxLaserRange if (self.position[1]-maxLaserRange) > 0 else 0
		maxy=self.position[1]+maxLaserRange if (self.position[1]+maxLaserRange) < envmap.shape[1] else envmap.size[1]

		print minx, maxx, miny, maxy
		rawSensing = envmap[minx:maxx, miny:maxy]
		print rawSensing
		print rawSensing.shape
	
