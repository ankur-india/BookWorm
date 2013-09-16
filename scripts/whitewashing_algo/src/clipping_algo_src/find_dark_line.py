import numpy as np
import csv as csv
from operator import itemgetter	#optional, required for method c

location  = "D:\\Dropbox\\ankur\\pixel_tests\\"  #file location
dataFile = "test.csv"
file = csv.reader(open(location+dataFile,"rb")) //read the information saved by "read_image_info.py"

data = []
for row in file:
    data.append(row)

upIndex = []
downIndex = []
prev = int(data[0][1]) -1
index = int(data[0][0])
downIndex.append(index)

#find indices of white gaps around and between lines
for row in data:
    if prev == int(row[1])-1 :
        prev = int(row[1])
        index = int(row[0])
        
    else :
        upIndex.append(index)
        downIndex.append(index+1)
        prev = int(row[1])

l = len(data) -1
index = int(data[l][0])
upIndex.append(index)

dark = []
size = np.size(upIndex)
#print size

for i in range(size):
    low = downIndex[i]
    high = int(upIndex[i])+1
    g = []
    k = []
    #print (low,high)
    g = data[low:high]
    #print g
    #k = sorted(g, key=lambda g:g[2]) # method a
    item = g[0]
    k=g[0][2]
    for row in g:
        if (int(k) > int(row[2])):
            item = row
            k = row[2]
    print item #method b
    
    #k = max(g, key =itemgetter(2)) #method c
    dark.append(k)
    
print dark
#write dark-line y-coordinates and pixelcount to a file
file2 = csv.writer(open("D:\\Dropbox\\ankur\\pixel_tests\\test_dark.csv","wb"))
for each in dark:
    file2.writerow(each)