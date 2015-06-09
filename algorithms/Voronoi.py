#!/usr/bin/python

import math
import numpy as np

nbLaserDir = 8 # This must not change
maxLaserRange = 20

class Voronoi:
	def __init__(self):
		self.position=(50, 50)
		self.centerList=[self.position]
		self.activeCenter=0
		self.edgeList=[]
		self.speed =(0,0)
		self.centerWidth = 10.0
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
		#print "Sensing ..."
		leftMinX=self.position[0]-1-maxLaserRange if (self.position[0]-1-maxLaserRange) >= 0 else 0
		leftMaxX=self.position[0]-1 if (self.position[0]-1) >= 0 else 0
		
		rightMinX=self.position[0]+1 if (self.position[0]+1) < envmap.shape[0] else envmap.shape[0]
		rightMaxX=self.position[0]+1+maxLaserRange if (self.position[0]+1+maxLaserRange) < envmap.shape[0] else envmap.shape[0]
		
		topMinY=self.position[1]+1 if (self.position[1]+1) < envmap.shape[1] else envmap.shape[1]
		topMaxY=self.position[1]+1+maxLaserRange if (self.position[1]+1+maxLaserRange) < envmap.shape[1] else envmap.shape[1]
		
		downMinY=self.position[1]-1-maxLaserRange if (self.position[1]-1-maxLaserRange) >= 0 else 0
		downMaxY=self.position[1]-1 if (self.position[1]-1) >= 0 else 0

		#print "limits", leftMinX, leftMaxX, rightMinX, rightMaxX, topMinY, topMaxY, downMinY, downMaxY
		
		leftSensing= envmap[leftMinX:leftMaxX, self.position[1]]
		leftSensing=leftSensing[::-1]
		self.leftDist=next((i for i, x in enumerate(leftSensing) if x), np.inf)
		rightSensing=envmap[rightMinX:rightMaxX, self.position[1]]
		self.rightDist=next((i for i, x in enumerate(rightSensing) if x), np.inf)
		topSensing=envmap[self.position[0], topMinY:topMaxY]
		self.topDist=next((i for i, x in enumerate(topSensing) if x), np.inf)
		downSensing=envmap[self.position[0], downMinY:downMaxY] 
		downSensing=downSensing[::-1]
		self.downDist=next((i for i, x in enumerate(downSensing) if x), np.inf)
		self.sensors=[self.leftDist, self.rightDist, self.topDist, self.downDist]

		#print leftSensing, leftDist 
		#print rightSensing, rightDist
		#print topSensing, topDist
		#print downSensing, downDist 

	def distToActiveCenter(self):
		return math.sqrt(math.pow(self.position[0]-self.centerList[self.activeCenter][0],2)+math.pow(self.position[1]-self.centerList[self.activeCenter][1],2))

	def computeDistToCenters(self):
		self.distCenters=[math.sqrt(math.pow(cp[0]-self.position[0],2)+math.pow(cp[1]-self.position[1],2)) for cp in self.centerList]
		return self.distCenters

	def updateActiveCenter(self):
		self.activeCenter = self.activeCenter if len((np.where(self.distCenters == np.array(self.distCenters).min()))[0].tolist())>1 else ((np.where(self.distCenters == np.array(self.distCenters).min()))[0].tolist())[0]

	def moveTo(self, x, y):
		self.position=(x, y)
	
	def forwardDrive(self, envMap):
		self.senseLasers(envMap)
		#print type(envMap)
		randvalues=(np.random.rand(), np.random.rand())
		speedVar = 10
		self.speed = (math.floor(0.5*self.speed[0])+math.floor(speedVar*(randvalues[0]-0.4)), math.floor(0.5*self.speed[1])+math.floor(speedVar*((randvalues[1])-0.4)))
		posX=self.position[0] + self.speed[0]
		if ((posX < envMap.shape[0]) and (posX > 0)):
			posX = posX if (envMap[posX, self.position[1]] != 1) else self.position[0]
		else:
			posX=self.position[0]
		posY=self.position[1] + self.speed[1]
		if ((posY < envMap.shape[1]) and (posY > 0)):
			posY = posY if (envMap[self.position[0], posY] != 1) else self.position[1]
		else:
			posY=self.position[1]

		self.moveTo(posX, posY)
		# update center list and distances :
		#print "Distances to active center:",self.distToActiveCenter()
		self.computeDistToCenters()
		self.updateActiveCenter()
		print "Active center", self.activeCenter, self.distToActiveCenter()
		if self.distToActiveCenter() > self.centerWidth:
			self.centerList.append(self.position)
			self.computeDistToCenters()
			self.updateActiveCenter()



