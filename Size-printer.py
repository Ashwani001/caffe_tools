#Script to check and Print the size of all images stored in /home/ash/caffe/examples/images/google
#Makes it easy to know if all are correct size (256x256)

import os
from PIL import Image

for filename in os.listdir("/home/ash/caffe/examples/images/google"):
    #print  filename
    fullname = os.path.join('/home/ash/caffe/examples/images/google',filename)
    img = Image.open(fullname)
    print filename,"\t",img.size
    #print fullname
