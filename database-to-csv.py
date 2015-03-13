#Turns the caffe databse file into something tab and comma semerated (readble by csv proceesing tools)
#Output is cleaneddatabase.txt

text_file = open("/home/ash/database.txt", "r")#Output file name and location
lines = text_file.read().split('\n')
text_file.close()
i=1

f = open("/home/ash/cleaneddatabase.txt", "w")#Output file name and location
f.write('Serial\tFolder\tKey Words\n')

for line in lines:
    f.write(str(i)+'\t')
    f.write(str(line[:9])+'\t')
    f.write(line[10:]+'\n')
    i=i+1

f.close()
