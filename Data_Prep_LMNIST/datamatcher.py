#Reads in CSV
#Matches the three variables using the timestamp
#Prints 'NO' at missing values
#Input newdata.csv (see example)
#Outputs matcheddata.csv (see example)
import csv
import numpy as np

def importer(F):
	filename="/home/ash/Desktop/Car-data-"+F+".csv"
	text_file = open(filename, "r")
	F = text_file.read()#.split('\n')
	#print F
	text_file.close()

def csv_importer(X):
	filename="/home/ash/GitHub/Data_Prep_LMNIST/"+X+".csv"
	X = np.genfromtxt(filename,delimiter="\t",dtype=None)
	#print len(X)
	return X

allData=csv_importer("newdata")

i=no_angle=no_speed=no_accel=0

for line in allData:
	if(allData[i][0])!='':
		no_angle=no_angle+1
	if(allData[i][2])!='':
		no_speed=no_speed+1
	if(allData[i][4])!='':
		no_accel=no_accel+1
	i=i+1

dataX = [[0 for x in range(6)] for x in range(len(allData))] 
for i in range(0,len(dataX)):
	dataX[i][0]=allData[i][0]
	dataX[i][1]=allData[i][1]
	dataX[i][2]=dataX[i][3]=dataX[i][4]=dataX[i][5]='NO'

same_counter=0
for i in range(0,no_speed):
	for j in range(0,no_angle):
		if((allData[i][2])==(allData[j][0])):
			if((allData[i][2])==(allData[i-1][2])):
				same_counter=same_counter+1
			else:
				same_counter=0
			dataX[j+same_counter][2]=allData[i][2]
			dataX[j+same_counter][3]=allData[i][3]		
			break

same_counter=0		
for i in range(0,no_accel):
	for j in range(0,no_angle):
		if(str(allData[j][0])==str(allData[i][4])[1:]):
			if((allData[i][4])==(allData[i-1][4])):
				same_counter=same_counter+1
			else:
				same_counter=0
			dataX[j+same_counter][4]=str(allData[i][4])[1:]
			dataX[j+same_counter][5]=allData[i][5]		
			break

f = open("/home/ash/GitHub/Data_Prep_LMNIST/matcheddata.csv", "w")#Output file name and location
for i in range(0,no_angle):
	for j in range(0,5):
		f.write(str(dataX[i][j]))
		f.write('\t')
	f.write((dataX[i][5])+'\n')
f.close()
