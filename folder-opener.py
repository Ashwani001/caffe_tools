#To be run from terminal
#Allows you to enter filename and the folder will open up in finder
#Usage: python opener.py n00001
#Can edit using os.path.exists(path) if you want it to check for file existing or not

import sys
import os
fullname = '/home/ash/caffe/examples/imagenet/train_rest/' + str(sys.argv[1])
os.system('gnome-open {0}'.format(fullname))
# os.path.exists(path)
