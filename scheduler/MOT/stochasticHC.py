from scheduler.MOT.schedulerInterface import MOT
from scheduler.MOT._MOTHelper import _Helper
from datetime import date, datetime, timedelta
from random import shuffle,randint
from ..services import Services
import itertools
import sys

class MOTStochasticHC(MOT):

	def find(self,missionList):
		""" does not examine any neighbors before deciding how to move. 
		Rather, it selects a neighbor at random, and moves to that one
		if it is better."""

		usefulTime=6

		maxIterations = 50
		i=0
		oldScore = sys.maxsize  
		newOrder=[]
		bestNextPassList=[]
		

		nextPassListStart = _Helper.getPassesFromMissions(self, missionList)
		curOrder=list(nextPassListStart)
		print(" Starting stochastic hillclimbing")
		while i<maxIterations:
			
			#swap two random elements
			i1 = randint(0,len(curOrder)-1)
			i2 = randint(0,len(curOrder)-1)
			swap1 = curOrder[i1]
			swap2 = curOrder[i2]

			curOrder[i2]=swap1
			curOrder[i1]=swap2
			
			newScore,nextPassList = _Helper.fitnessFunction(self,curOrder,usefulTime)

			
			#Could make it so it only changes when it's a lot better or a little better
			if newScore < oldScore:
				#use that 
				oldScore=newScore
				bestOrder=list(curOrder)
				bestNextPassList=list(nextPassList)
				i=0
			else:
				i+=1
				#print(i)
			
			if (i%(maxIterations/10))==0:
				print(".")

		if i==maxIterations:
			print(" Stochastic HillClimbing finished with the order ")
			print("And a score of {}".format(oldScore))
			return bestNextPassList

