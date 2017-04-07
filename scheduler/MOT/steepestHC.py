from scheduler.MOT.schedulerInterface import MOT
from scheduler.MOT._MOTHelper import _Helper
from datetime import date, datetime, timedelta
from random import shuffle,randint
from ..services import Services
import itertools
import sys

class MOTSteepestHC(MOT):

	def find(self,missionList):
		""" In steepest hill climbing, the neighbour that has the best score is used"""
		
		usefulTime=6
		bestNextPassList=[]
		print(" Starting steepest hillclimbing")
		maxIterations = 50
		#maxNeighbours=5000
		i=0
		oldScore = sys.maxsize
		newScore=0
		newOrder=[]

		nextPassListStart=[]
		for mission in missionList:
			nextPass = Services.getNextPass(self, mission.TLE ,mission, datetime.utcnow())
			#print(nextPass)
			dur=nextPass.setTime - nextPass.riseTime
			# if(dur<timedelta(0)):
			# 	print(nextPass.tle.name)
			nextPassListStart.append(nextPass)

		curOrder=list(nextPassListStart)


		while i<maxIterations:
			listOfNearestNeighboursAndItself=[]
			generatorOfAllNeighboursIncItself = itertools.permutations(curOrder)

			oldNeighbourScore=sys.maxsize
			for neighbour in generatorOfAllNeighboursIncItself:

				newNeighbourScore,nextPassList  = _Helper.fitnessFunction(self,neighbour,usefulTime)

				if(newNeighbourScore < oldNeighbourScore):
					curOrder=neighbour
					oldNeighbourScore=newNeighbourScore
					newScore=newNeighbourScore
					break;

			if newScore < oldScore:
				oldScore=newScore
				bestOrder = list(curOrder)
				bestNextPassList = list(nextPassList)
				i=0
			else:
				i+=1
			#print(newScore)

			if (i%(maxIterations/10))==0:
				print(".")
				
		if i==maxIterations:
			print("Steepest HillClimbing finished with the order ")
			# for n in curOrder:
			# 	pass
			# 	print(n)
			#print("{} curOrder could be global maxima with a score of {}".format(curOrder,oldScore))		
			print("And a score of {}".format(oldScore))
			return oldScore,bestNextPassList

