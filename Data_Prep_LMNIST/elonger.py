#Reads in CSV (created using datamatcher.py)
#Prints previous value wherever there is NO present, hence "elonging" the time axis to match longest one
#Input newdata.csv (see example)
#Outputs readydata.csv (see example)

import csv
import numpy as np


filename="/home/ash/Desktop/matcheddata.csv"
Z = np.genfromtxt(filename,delimiter="\t",dtype=None)
#print len(Z)

dataZ = [[0 for x in range(4)] for x in range(len(Z))] 
for i in range(0,len(dataZ)):
	dataZ[i][0]=Z[i][0]
	dataZ[i][1]=Z[i][1]
	dataZ[i][2]=dataZ[i][3]='NO'


for i in range(0,len(Z)):
	if((Z[i][2])=='NO'):
		dataZ[i][2]=dataZ[i-1][2]		
	else:
		dataZ[i][2]=Z[i][3]		


for i in range(0,len(Z)):
	if((Z[i][4])=='NO'):
		dataZ[i][3]=dataZ[i-1][3]		
	else:
		dataZ[i][3]=Z[i][5]


f = open("/home/ash/Desktop/readydata.csv", "w")#Output file name and location
for i in range(0,len(Z)):
	for j in range(0,3):
		f.write(str(dataZ[i][j]))
		f.write('\t')
	f.write((dataZ[i][3])+'\n')
f.close()
