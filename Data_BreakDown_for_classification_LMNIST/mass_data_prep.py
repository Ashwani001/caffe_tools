#time is taken at 2dp, but not rounded up (round up for better accuracy)

import os
import csv
import numpy as np

def csv_importer(X):#to read the csv
	Y = np.genfromtxt(X,delimiter=",",dtype=str)#None)
	return Y

def leanify(allData):
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

	for z in range(0,6):
		dataX[0][z]=allData[0][z]

	for i in range(1,len(dataX)):
		dataX[i][0]=allData[i][0][:(allData[i][0].find('.'))+3]
		dataX[i][1]=allData[i][1]
		dataX[i][2]=dataX[i][3]=dataX[i][4]=dataX[i][5]='NO'
	
	same_counter=0
	for i in range(1,no_speed):
		for j in range(1,no_angle):
			dot=(allData[i][2].find('.'))+3
			if((allData[i][2][:dot])==(dataX[j][0])):
				if((allData[i][2][:dot])==(allData[i-1][2][:dot])):
					same_counter=same_counter+1
				else:
					same_counter=0
				dataX[j+same_counter][2]=allData[i][2][:dot]
				dataX[j+same_counter][3]=allData[i][3]		
				break

	same_counter=0		
	for i in range(1,no_accel):
		for j in range(1,no_angle):
			dot=(allData[i][4].find('.'))+3
			if(dataX[j][0]==(allData[i][4])[:dot]):
				if((allData[i][4][:dot])==(allData[i-1][4][:dot])):
					same_counter=same_counter+1
				else:
					same_counter=0
				dataX[j+same_counter][4]=allData[i][4][:dot]
				dataX[j+same_counter][5]=allData[i][5]		
				break

	return dataX

def no_no(Z,filename):

	dataZ = [[0 for x in range(4)] for x in range(len(Z))] 
	for i in range(0,len(dataZ)):
		dataZ[i][0]=Z[i][0]#time
		dataZ[i][1]=Z[i][1]#angle
		dataZ[i][2]=dataZ[i][3]='NO'

	x2=x3=0
	for x in range(1,len(Z)):
		#print x,Z[x]
		if Z[x][3]=='NO':
			x2=x2+1
		else: break
	for x in range(1,len(Z)):
		if Z[x][5]=='NO':
			x3=x3+1
		else: break

	dataZ[0][2]=Z[0][3]
	dataZ[0][3]=Z[0][5]
	dataZ[1][2]=Z[x2+1][3]
	dataZ[1][3]=Z[x3+1][5]
	#print x2,x3
	
	for i in range(2,len(Z)):#speed
		if((Z[i][2])=='NO'):
			dataZ[i][2]=dataZ[i-1][2]		
		else:
			dataZ[i][2]=Z[i][3]		

	for i in range(2,len(Z)):#accelerator
		if((Z[i][4])=='NO'):
			dataZ[i][3]=dataZ[i-1][3]		
		else:
			dataZ[i][3]=Z[i][5]

	filelocation="/home/ash/Desktop/processed_data_set/"+filename+"_final.csv"
	f = open(filelocation, "w")#Output file name and location	
	for i in range(0,len(Z)):
		for j in range(0,3):
			f.write(str(dataZ[i][j]))
			f.write('\t')
		f.write((dataZ[i][3])+'\n')
	f.close()

	return dataZ

def breaker(Z,desired,filename):
	lenz=[0 for x in range(len(Z))]
	secs=1
	
	lenz[1]=1
	for i in range(2,len(Z)):
		if Z[i][0][:Z[i][0].find('.')]!=Z[i-1][0][:Z[i-1][0].find('.')]:
			secs=secs+1
		lenz[i]=secs

	clones=secs-desired+1

	for x in range(1,clones+1):#number of files to output
		filelocation="/home/ash/Desktop/processed_data_set/"+filename+"_test_"+str(x)+".csv"
		f = open(filelocation, "w")#Output file name and location
		for u in range(0,10):#10 is number of secs we want...there is a variable for this, change it
			for y in range(0,len(Z)):#super inefficient...can it be changed? Should start at the new t-second, end when it stops
				if(lenz[y]==(x+u)):#checks the t-second (1 to 21)
					for w in range(0,4):#outputs the four variables
						f.write(str(Z[y][w])+'\t')
					f.write('\n')
		f.close()


#############################################################################################
#							End of function declaration										#	#############################################################################################

a=csv_importer("/home/ash/Desktop/unprocessed_data_set/1.csv")
b=leanify(a)
c=no_no(b,str(1))
breaker(c,10,str(1))
