#A script written for caffe example 2
#Processes all images stored at /home/ash/caffe/examples/images
#Outputs summary.txt
#Lets you compare the actual file name to the prediction name (pulled from database)

#Updated to print size (testing different sizes now)
#Corrected reference number(case 0 was being left out previously)
#Reordered layout
#Corrected spacing, so make it easier to read visually
#Also writes out another file which is useful for CSV processing(tab seperated here)
#Broke program up into functions for reasy reading

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
caffe_root = '/home/ash/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe

def dataprep():
	text_file = open("/home/ash/database.txt", "r")#this file is a copy of caffe/data/ilsvrc12/synset_words.txt
	lines = text_file.read().split('\n')
	text_file.close()
	i=0
	
	#mydata will be used in another function hence global	
	global mydata
	mydata = [[0 for x in range(3)] for x in range(len(lines))]
	for line in lines:
		mydata[i][0]=i
		mydata[i][1]=line[10:]
		mydata[i][2]=line[:9]
		i=i+1

def caffeprep():
	#net will be used in another function hence global
	global net	
	MODEL_FILE = '/home/ash/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
	PRETRAINED = '/home/ash/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
	np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)
	caffe.set_mode_cpu()
	net = caffe.Classifier(MODEL_FILE, PRETRAINED)
	net.set_raw_scale('data',255)
	net.set_channel_swap('data',(2,1,0))
	net.set_mean('data',np.load(caffe_root+'python/caffe/imagenet/ilsvrc_2012_mean.npy'))

def looper():
	for filename in os.listdir("/home/ash/caffe/examples/images"):
		#Image.open() needs the full directory, so we join the filename
		IMAGE_FILE = os.path.join('/home/ash/caffe/examples/images',filename)
		img = Image.open(IMAGE_FILE)
		#Next we feed caffe the image
		input_image = caffe.io.load_image(IMAGE_FILE)
		#overpredict
		prediction = net.predict([input_image])
		#centerpredict, only looks at the center
		prediction1 = net.predict([input_image], oversample=False)
		#We assign the values to appropriately named variables
		overvalue=prediction[0].argmax()
		centervalue=prediction1[0].argmax()
		#This boolean will be used in an upcoming loop	
		centertrue=overtrue=0
		#This loop helps to search for the match in the database
		#and stores the folder name as well as the description
		for j in range(0,999):
		    if str(mydata[j][0])==str(overvalue):
		        overname=str(mydata[j][1])
		        overlocation=str(mydata[j][2])
		        overtrue=1
		    if str(mydata[j][0])==str(centervalue):
		        centername=str(mydata[j][1])
		        centerlocation=str(mydata[j][2])
		        centertrue=1
		    if (centertrue==1)&(overtrue==1):
		        break

		#writing to summary.txt
		line_new = '{:>5}  {:>9}  {:>12} {:>25} {:>12} {:>5}'.format( overlocation, 'Over', str(img.size),filename, str(overvalue)+'\t', overname)
		f.write(line_new+'\n')
		line_new = '{:>5}  {:>9}  {:>12} {:>25} {:>12} {:>5}'.format(centerlocation, 'Center', str(img.size), filename, str(centervalue)+'\t',centername )
		f.write(line_new+'\n\n')
		#Writing to summary-csv.txt
		fcsv.write(overlocation+'\tOver\t'+str(img.size)+'\t'+filename+'\t'+str(overvalue)+'\t'+overname+'\n')
		fcsv.write(centerlocation+'\tCenter\t'+str(img.size)+'\t'+filename+'\t'+str(centervalue)+'\t'+centername+'\n')


#####################################################################################################################################
#									Start of main program																			#			
#####################################################################################################################################

#Preparing data and initializing caffe
dataprep()
caffeprep()

#f will handle all fstream operations to summary.txt
f = open("/home/ash/summary1.txt", "w")
line_new = '{:>5}  {:>12}  {:>12} {:>25} {:>12} {:>5}'.format('Folder','Type','Size','Filename','Prediction\t','Answer\n')
#Writing header for summary.txt
f.write(line_new)

#fcsv will handle all fstream operations to summary-csv.txt
fcsv= open("/home/ash/summary-csv","w")
#Writing header for summary-csv.txt
fcsv.write('Folder\tType\tSize\tFilename\tPrediction\tAnswer\n')

looper()

#Closing streams
f.close()

##End of program
fcsv.close()
