#Script to go into each subfolder in /home/ash/caffe/examples/images/Non-Processed
#and rename all images in the subfolder to contain the subfolder name and a unique number identifier
#Also checks and prints the sizes

import os
from PIL import Image

for files in os.listdir("/home/ash/caffe/examples/images/Non-Processed"):
	#Take note of what currentfolder is; full address of subfoler
	currentfolder= os.path.join('/home/ash/caffe/examples/images/Non-Processed',files)
	i=0
	for f in os.listdir(currentfolder):
		fullname = os.path.join(currentfolder,f)#full address of image, old name
		newname= files+str(i)#image is given name of the folder plus a unique numer(unique to that folder)
		fullnewname = os.path.join(currentfolder,newname)#full address of image, new name
		os.rename(fullname,fullnewname)
		img = Image.open(fullnewname)
		print newname,"\t",img.size
		i=i+1
