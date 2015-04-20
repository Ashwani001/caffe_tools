"""
Generate data used in the HDF5DataLayer test.
"""
import os
import numpy as np
import h5py
###################################################################################

def csv_importer(y):
	filename="/home/ash/Desktop/test/"+y+".csv"#location of file
	X = np.genfromtxt(filename,delimiter="\t",dtype=None)
	return X

allData=csv_importer("readydata")#passes file name

###################################################################################

num_cols = 3
num_rows = (len(allData)-1)# -1 as the headings are not needed
height = 1
width = 1
total_size = num_cols * num_rows * height * width

data = np.arange(total_size)#initializing data set
data = data.reshape(num_rows, num_cols, height, width)
data = data.astype('float32')#all data here are of same type
#call data using data[col][row]

for i in range(0,len(allData)-1):
	data[i][0]=allData[i+1][1]
	data[i][1]=allData[i+1][2]
	data[i][2]=allData[i+1][3]

###################################################################################

#label starts with 1, apparently there is some error with 0
label = 1 + np.arange(num_rows)[:, np.newaxis]#'1' so that indexing starts at 1
label = label.astype('str')#float32')

###################################################################################

with h5py.File(os.path.dirname(os.path.abspath(__file__)) + '/car_data.h5', 'w') as f:
    f['data'] = data
    f['label'] = label

with h5py.File(os.path.dirname(os.path.abspath(__file__)) + '/car_data_2_gzip.h5', 'w') as f:
    f.create_dataset(
        'data', data=data + total_size,
        compression='gzip', compression_opts=1
    )

with open(os.path.dirname(os.path.abspath(__file__)) + '/car_data_list.txt', 'w') as f:
    f.write(os.path.dirname(os.path.abspath(__file__)) + '/car_data.h5\n')
    f.write(os.path.dirname(os.path.abspath(__file__)) + '/car_data_2_gzip.h5\n')
