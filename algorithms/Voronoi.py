#!/usr/bin/python

import math
import numpy as np

nbLaserDir = 8 # This must not change
maxLaserRange = 15

class Voronoi:
	def __init__(self):
		self.centerList=[]
		self.activeCenter=0
		self.edgeList=[]
		self.position=(72, 82)
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
		leftMinX=self.position[0]-1-maxLaserRange if (self.position[0]-1-maxLaserRange) >= 0 else 0
		leftMaxX=self.position[0]-1 if (self.position[0]-1) >= 0 else 0
		
		rightMinX=self.position[0]+1 if (self.position[0]+1) < envmap.shape[0] else envmap.shape[0]
		rightMaxX=self.position[0]+1+maxLaserRange if (self.position[0]+1+maxLaserRange) < envmap.shape[0] else envmap.shape[0]
		
		topMinY=self.position[1]+1 if (self.position[1]+1) < envmap.shape[1] else envmap.shape[1]
		topMaxY=self.position[1]+1+maxLaserRange if (self.position[1]+1+maxLaserRange) < envmap.shape[1] else envmap.shape[1]
		
		downMinY=self.position[1]-1-maxLaserRange if (self.position[1]-1-maxLaserRange) >= 0 else 0
		downMaxY=self.position[1]-1 if (self.position[1]-1) >= 0 else 0

		print "limits", leftMinX, leftMaxX, rightMinX, rightMaxX, topMinY, topMaxY, downMinY, downMaxY
		leftSensing= envmap[leftMinX:leftMaxX, self.position[1]]
		leftSensing=leftSensing[::-1]
		self.leftDist=next((i for i, x in enumerate(leftSensing) if x), np.inf)
		#print leftSensing, leftDist 

		rightSensing=envmap[rightMinX:rightMaxX, self.position[1]]
		self.rightDist=next((i for i, x in enumerate(rightSensing) if x), np.inf)
		#print rightSensing, rightDist
		
		topSensing=envmap[self.position[0], topMinY:topMaxY]
		self.topDist=next((i for i, x in enumerate(topSensing) if x), np.inf)
		#print topSensing, topDist

		downSensing=envmap[self.position[0], downMinY:downMaxY] 
		downSensing=downSensing[::-1]
		self.downDist=next((i for i, x in enumerate(downSensing) if x), np.inf)
		#print downSensing, downDist 

	def distToActiveCenter(self):
		return math.sqrt(math.pow(self.position[0]-self.centerList[self.activeCenter][0],2)+math.pow(self.position[1]-self.centerList[self.activeCenter][1],2))

#	def distToCenters(self):
#		return math.sqrt(math.pow(self.position[::][0]-self.centerList[0],2)+math.pow(self.position[1]-self.centerList[::][1],2))

