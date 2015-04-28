################################################################################################
#time is taken at 2dp, but not rounded up (round up for better accuracy)
################################################################################################
#
#Function: csv_importer(X,sep)
#	Parameters: 
#		X - Location of csv file 
#		sep - seperator; either '\t' or ','
#	Retuns: Raw data in array form
#	Purpose: Reads in the raw data, in form of CSV and returns an array with it
#	Comments: For format of raw data, refer to /unprocessed_data/1.csv
#
################################################################################################
#
#Function: leanify(allData)
#	Parameters: 
#		allData - array from previous function
#	Returns: array of data with variables matched to timestamp 
#			 follows the format of - timestamp, variable 1,variable 2,variable 3
#	Purpose: To match variable 2 and 3 to timestamp in column 1
#	Comments: -
#
################################################################################################
#
#Function: no_no(Z,filename)
#	Parameters:
#		Z - array from previous function
#		filename - identifier for this batch of files
#	Returns: 
#		Array with full data (no more NOs)
#		Outputs a file - /home/ash/Desktop/processed_data_set/"+filename+"_final.csv
#	Purpose: To extend data for variables with lower sampling rate 
#			 Produces matching data for each instance of variable with the highest sampling rate
#	Comments: The output file is just for reference. That portion can be removed.
#
################################################################################################
#
#Function: breaker(Z,desired,filename)
#	Parameters: 
#		Z - array from previous function
#		filename - identifier for this batch of files
#		desired - how many seconds do you want per data set?
#	Returns: Outputs multiple files, each file with desired number of seconds
#	Purpose: Fufill the purpose of the whole script
#	Comments: -
#
################################################################################################

import os
import csv
import numpy as np

def csv_importer(X,sep):
	Y = np.genfromtxt(X,delimiter=str(sep),dtype=str)
	return Y

def leanify(allData):
	i=no_angle=no_speed=no_accel=0#tracks the number of entries for each variable

	for line in allData:# 0,2,4 or 1,3,5 are both fine
		if(allData[i][0])!='':#as long as it is not empty, increment
			no_angle=no_angle+1
		if(allData[i][2])!='':
			no_speed=no_speed+1
		if(allData[i][4])!='':
			no_accel=no_accel+1
		i=i+1#i would be the same as variable with highest sampling rate
	
	dataX = [[0 for x in range(6)] for x in range(len(allData))] #declaring 2d array

	for z in range(0,6):
		dataX[0][z]=allData[0][z]#copies the first row over, the headings

	for i in range(1,len(dataX)):
		dataX[i][0]=allData[i][0][:(allData[i][0].find('.'))+3]#Copy over time with 2dp #0 due to assumption stated below
		dataX[i][1]=allData[i][1]#copy over the first vairable. This is becuase angle has the highest sampling rate
		dataX[i][2]=dataX[i][3]=dataX[i][4]=dataX[i][5]='NO'
	
	#the following part of the code is a little complex
	#for the data I am using it is not necessary as viables 2 and 3 sampling rate is much lower than variable 1
	#simplify it if necessary
	same_counter=0
	for i in range(1,no_speed): 
		for j in range(1,no_angle): 
			dot=(allData[i][2].find('.'))+3
			if((allData[i][2][:dot])==(dataX[j][0])):#if the time matches
				if((allData[i][2][:dot])==(allData[i-1][2][:dot])): #by right the second dot should be changed to (allData[i-1][2].find('.'))+3
					same_counter=same_counter+1#data with the same time tag
				else:
					same_counter=0#a new time tag
				dataX[j+same_counter][2]=allData[i][2][:dot]#if same_counter is not used, new data will overwrite the first occurance of the time stamp (more than one data for one timestamp)
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

	dataZ = [[0 for x in range(4)] for x in range(len(Z))] #declaring a new 2d array
	for i in range(0,len(dataZ)):
		dataZ[i][0]=Z[i][0]#copy over time
		dataZ[i][1]=Z[i][1]#copy over angle
		dataZ[i][2]=dataZ[i][3]='NO'#chage the other two to NO (can leave as 0 but I found NO easier to read when testing and debugging)


	dataZ[0][2]=Z[0][3]#copy over the headings
	dataZ[0][3]=Z[0][5]

	#the following chunk of code gets the first instance of data for variable 2 and 3 and puts them as the second row
	#otherwise you might find the titles appearing in the row untilt he first instance of data is reached
	x2=x3=0 
	for x in range(1,len(Z)):
		if Z[x][3]=='NO':
			x2=x2+1
		else: break
	for x in range(1,len(Z)):
		if Z[x][5]=='NO':
			x3=x3+1
		else: break
	dataZ[1][2]=Z[x2+1][3]
	dataZ[1][3]=Z[x3+1][5]

	#the following chunk of code replaces the NOs with the last captured data
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
	secs=1#will keep track of number of unique seconds
	lenz=[0 for x in range(len(Z))]#will keep track of which t-second the row(in Z) belongs to
	
	lenz[1]=1#due to method used below, this needs to be filled seperatly 
	for i in range(2,len(Z)):
		if Z[i][0][:Z[i][0].find('.')]!=Z[i-1][0][:Z[i-1][0].find('.')]:
			secs=secs+1
		lenz[i]=secs

	clones=secs-desired+1#clones will be the number of files to output

	for x in range(1,clones+1):
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
#							End of function declaration										#
#############################################################################################

a=csv_importer("/home/ash/Desktop/unprocessed_data_set/1.csv",',')
b=leanify(a)
c=no_no(b,str(1))
breaker(c,10,str(1))
