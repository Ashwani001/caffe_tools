import os
import csv
import numpy as np

def csv_importer(filename,sep):
	filelocation="/home/ash/Desktop/csv_tempt/"+filename+".csv"
	Y = np.genfromtxt(filelocation,delimiter=str(sep),dtype=str)
	
	f = open(filelocation, "w")#Output file name and location	

	f.write('Time')
	f.write('\t')
	f.write(str(Y[0][5]))
	f.write('\t')
	f.write('Time')
	f.write('\t')
	f.write(str(Y[0][2]))
	f.write('\t')
	f.write('Time')
	f.write('\t')
	f.write(str(Y[0][8]))
	f.write('\t')
	f.write('Time')
	f.write('\t')
	f.write((Y[0][11])+'\n')


	for i in range(1,len(Y)):
		f.write(str(Y[i][4]))
		f.write('\t')
		f.write(str(Y[i][5]))
		f.write('\t')
		f.write(str(Y[i][1]))
		f.write('\t')
		f.write(str(Y[i][2]))
		f.write('\t')
		f.write(str(Y[i][7]))
		f.write('\t')
		f.write(str(Y[i][8]))
		f.write('\t')
		f.write(str(Y[i][10]))
		f.write('\t')
		f.write((Y[i][11])+'\n')
	f.close()


#############################################################################################
#							End of function declaration										#
#############################################################################################

for x in range(1,5):
	csv_importer(str(x),',')

