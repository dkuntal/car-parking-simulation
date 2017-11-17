import threading
from queue import Queue
from random import randint
import time

import numpy as np
import param


def servWtTime(servedCar):
	# # print(servedCar)
	# tempCarList = np.array(servedCar)
	# # print(tempCarList)
	# tempCarList = tempCarList.transpose()
	# # print(tempCarList)
	# serveTime = tempCarList[1]
	totalTime = 0
	for carSeq in range(len(servedCar)):
		# print(servedCar[carSeq][1])
		# print(servedCar[carSeq][0][1])
		totalTime += servedCar[carSeq][1] - servedCar[carSeq][0][1]
	print('totalTime',totalTime,'_ avg serve time',totalTime/len(servedCar))

def frustLeave(leftCar):
	carN = param.carN

	totalTime = 0
	for carSeq in range(len(leftCar)):
		totalTime += leftCar[carSeq][1] - leftCar[carSeq][0][1]
	print('Avg leave time',totalTime/len(leftCar),'_ Leave rate',len(leftCar)/carN)



def simulator1mSIRO(car,parkSlotN):
	t = 0
	q = []
	vacParkSpot = parkSlotN
	servedCar = []
	leftCar = []

	testN = 0

	parkSpot = []
	# for i in range(parkSlotN):
	# 	parkSpot.append([-1,-1])

	# print('Outside 1st while')

	while True:
		# print('inside while')
		while True:
			try:	# Car arrival to Queue
				if car[0][1] <= t:
					# print(car[0][1],t)
					tempCar = car.pop(0)
					q.append(tempCar)
					# print('car',tempCar[0],'comes at ',t) ###########
				else:
					break

			except Exception:
				break
			# print('inside car arrival while')

		# while True:
			# print('Inside served car out loop')
		try:	# Served car gets out
			for i in range(len(parkSpot)):
				# print('len(parkSpot)',len(parkSpot))
				if parkSpot[i][0][3] + parkSpot[i][1] <= t:
					temp = parkSpot.pop(i)
					i -= 1
					vacParkSpot += 1
					# print('Car',temp[0][0],'service completes at ',t) #######
					testN += 1
				else:
					pass
						# break

		except Exception:
			pass
				# break
			# print('Inside served car out loop 2')

		# while True:	# Car parked from Queue
			# print('Inside car parked from queue loop')
		try:
			while vacParkSpot > 0:
				randID = randint(0,len(q)-1)
				# print('Served randID',randID,q)
				randCar = q.pop(randID)
				parkSpot.append([randCar,t])
				vacParkSpot -= 1
				# print('Car',randCar[0],'parked at ',t) ##############
				# print(randCar)
				# print(servedCar)
				servedCar.append([randCar,t])


		except Exception:
				# break
			pass

			# print('Inside car parked from queue loop 2')

		# while True:	# Frust driver gets out
			# print('Inside frust driver gets out loop')
		try:
			for i in range(len(q)):
				if t >= q[i][1] + q[i][2]:
					temp = q.pop(i)
					i += 1
					# print('Frust driver',temp[0],'leaves at ',t) ######
					testN += 1
					leftCar.append([temp,t])

		except Exception:
			pass
			# print('Inside frust driver gets out loop 2')

		# print(parkSpot,parkSlotN)
		# print('t',t,', testN',testN)
		t += 1
		if testN >= param.carN:
			break
	return servedCar,leftCar