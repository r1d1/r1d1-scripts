#!/usr/bin/python

import math
import numpy as np

nbLaserDir = 8 # This must not change
maxLaserRange = 10

class Voronoi:
	def __init__(self):
		self.centerList=[]
		self.edgeList=[]
		self.position=(99, 92)
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
		print "Sensing ..."
		# local estimation :
		localMap = np.ones((2*maxLaserRange+1, 2*maxLaserRange+1))
		#print localMap
		# measurement :
		print "shapes env, localmap:",envmap.shape, localMap.shape,"position:", self.position
		minx=self.position[0]-maxLaserRange-1 if (self.position[0]-maxLaserRange-1) > 0 else 0
		maxx=self.position[0]+maxLaserRange if (self.position[0]+maxLaserRange) < envmap.shape[0] else envmap.shape[0]
		miny=self.position[1]-maxLaserRange-1 if (self.position[1]-maxLaserRange-1) > 0 else 0
		maxy=self.position[1]+maxLaserRange if (self.position[1]+maxLaserRange) < envmap.shape[1] else envmap.shape[1]

		print "limits",minx, maxx, miny, maxy
		rawSensing = envmap[minx:maxx, miny:maxy]
		print rawSensing
		print rawSensing.shape
		#print "raw sensing",rawSensing.shape
		xc=math.ceil((maxx-minx)/2.0)
		yc=math.ceil((maxy-miny)/2.0)
		print "center", xc, yc, minx+xc, miny+yc
	#	print "borders", xc-rawSensing.shape[0]/2, (xc+rawSensing.shape[0]/2)
	#	print "borders", yc-rawSensing.shape[1]/2, (yc+rawSensing.shape[1]/2)
	#	print minx+maxLaserRange+1, miny+maxLaserRange+1
	#	localMap[(xc-rawSensing.shape[0]/2):(xc+rawSensing.shape[0]/2), (yc-rawSensing.shape[1]/2):(yc+rawSensing.shape[1]/2)]=rawSensing
#		print localMap


