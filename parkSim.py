import threading
from queue import Queue
import time

import numpy as np
import param
import sim

thread_lock = threading.Lock()
carQ = Queue()
carID = 0

# def arrThreader(arr):
# 	while True:
# 		try:
# 			time.sleep(arr[carID])
# 			carQ.put(carID)
# 		except:
# 			print('Arrival time error in "arrThreader(arr)"')

def merger(arr,fTimes,sTimes):
	time = 0-arr[0]
	# carID = 0
	carN = len(arr)
	car = []

	for carID in range(carN):
		print(time)
		car.append([carID,time+arr[carID],fTimes[carID],sTimes[carID]])
		time += arr[carID]

	return car

def main():
	arr = param.arrivals()
	# print(arr)

	fTimes = param.fTime()
	# print(fTimes)

	sTimes = param.sTime()
	# print(sTimes)

	car = merger(arr,fTimes,sTimes)

	# print(car)
	# servedCar = []
	# leftCar = []
	servedCar, leftCar = sim.simulator1mSIRO(car,param.parkSlotN)

	# # car arrival queue
	# arrThread = threading.Thread(target = arrThreader(arr))
	# arrThread.daemon = True
	# arrThread.start()

	# print(servedCar)
	sim.servWtTime(servedCar)
	# print(leftCar)
	sim.frustLeave(leftCar)

	

if __name__ == '__main__':
    main()