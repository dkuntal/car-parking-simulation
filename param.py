import numpy as np

"""
ALL UNITS ARE GIVEN
time = minute
length = meter

"""
carN = 100000	# 240/day
parkSlotN = 10

# Car arrival || Exponential || e^(-x)
arrExpMean = 2
arrExpRep = 1

# Frustration time || Uniform
fTimeUniLow = 5
fTimeUniHigh = 16

# Park Service Time || Exponential
sTimeExpMean = 60
sTimeExpRep = 1

# Parking dimensions
parkL = 2.4384	# 8 feet
parkW = 1.8288	# 6 feet

# Car arrival || Exponential || e^(-x)
def arrivals():
	return np.random.exponential(arrExpMean,(arrExpRep,carN))[0]

def fTime():
	return np.random.uniform(fTimeUniLow,fTimeUniHigh,carN)

def sTime():
	return np.random.exponential(sTimeExpMean,(sTimeExpRep,carN))[0]