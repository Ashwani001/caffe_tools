#Script to resize all images stored in /home/ash/caffe/examples/images
#Makes it easy to know if all are correct size (256x256)

import os
from PIL import Image

for filename in os.listdir("/home/ash/caffe/examples/images"):
    fullname = os.path.join('/home/ash/caffe/examples/images',filename)
    img = Image.open(fullname)
    img = img.resize((128,128), Image.ANTIALIAS)#(basewidth,hsize)
    dot=fullname.find('.')#checking for extensions in filename
    if(dot!=-1):
        transname=fullname[:dot]
    else:
        transname=fullname
    newname=transname+'.jpg'#file extension chosen is JPEG
    os.remove(fullname)#deletes old image
    img.save(newname)#saves new image
    print newname,"\t",img.size

#ANTIALIAS:
#The filter argument can be one of NEAREST, BILINEAR, BICUBIC, or ANTIALIAS (best quality).
# If omitted, it defaults to NEAREST.



