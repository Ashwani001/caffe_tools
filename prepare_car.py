#This contrains scrips used to preapre car detection database

#1	prep_train_txt(c,nc) #517 for 516 cars
#	Prepapres car_train.txt #c=no. of car pics, nc=no. of noncar pics
#
#2	synset_txt(c,nc)
#	Prepares synset.txt
#
#3	synset_words_txt(c,nc)
#	Prepares synset_words.txt
#
#4	img_preparer(basewidth=128,hsize=128,ext=jpeg,folder="/home/ash/caffe/examples/images")
#	resizes all images in 'folder' to basewidthxhsize, deletes old img and saves as imgname.'ext'
#
#5	img_rename(keyword='notcar',folder="/home/ash/caffe/examples/images,ext='jpeg'")
#	renames all imaged in 'folder' to 'keyword'+index.jpeg

import os
from PIL import Image

def prep_train_txt(c,nc):#517 for 516 cars,107 for 106 notcars
	f=open("car_train.txt","w")#imgs are already named nicely
	for i in range(1,c):
		zeros='0'*(4-len(str(i)))#this generates the zeroes infront of i
		f.write("car_"+zeros+str(i)+".ppm 0\n")#we will let 0 represent car
	for j in range(1,nc):
		zeros='0'*(4-len(str(j)))#this generates the zeroes infront of i
		f.write("notcar_"+zeros+str(j)+".jpeg 1\n")#we will let 1 represent notcar
	f.close()

def synset_txt(c,nc):
	f=open("synset.txt","w")#imgs are already named nicely
	for i in range(1,c):
		zeros='0'*(4-len(str(i)))#this generates the zeroes infront of i
		f.write("car_"+zeros+str(i)+".ppm\n")
	for j in range(1,nc):
		zeros='0'*(4-len(str(j)))#this generates the zeroes infront of i
		f.write("notcar_"+zeros+str(j)+".jpeg\n")
	f.close()

def synset_words_txt(c,nc):
	f=open("synset_words.txt","w")#imgs are already named nicely
	for i in range(1,c):
		zeros='0'*(4-len(str(i)))#this generates the zeroes infront of i
		f.write("car_"+zeros+str(i)+".ppm Car\n")
	for j in range(1,nc):
		zeros='0'*(4-len(str(j)))#this generates the zeroes infront of i
		f.write("notcar_"+zeros+str(j)+".jpeg Not Car\n")
	f.close()
	
def img_preparer(basewidth=128,hsize=128,ext='jpeg',folder="/home/ash/caffe/examples/images"):#resizes, gives new extention and deltes old imgs
	for filename in os.listdir(folder):
		fullname = os.path.join(folder,filename)
		#If converting gif to jpeg you need to convert the image to RGB mode.
		#Use: Image.open('old.gif').convert('RGB').save('new.jpeg')
		img = Image.open(fullname)
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		dot=fullname.find('.')#checking for extensions in filename
		if(dot!=-1):
			transname=fullname[:dot]
		else:
			transname=fullname
		newname=transname+'.'+ext#file extension default is jpeg
		os.remove(fullname)#deletes old image
		img.save(newname)#saves new image
		print newname,"\t",img.size

def img_rename(keyword='notcar',folder="/home/ash/caffe/examples/images",ext='jpeg'):
	i=1
	for f in os.listdir(folder):
		fullname = os.path.join(folder,f)#full address of image, old name
		newname= keyword+'_'+('0'*(4-len(str(i))))+str(i)+ext
		newfullname=os.path.join(folder,newname)
		os.rename(fullname,newfullname)
		img = Image.open(newfullname)
		print newname,"\t",img.size
		i=i+1


prep_train_txt(517,107) #517 for 516 cars
synset_txt(517,107)
synset_words_txt(517,107)
