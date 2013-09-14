# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Perform WhiteWashing on Image

# <headingcell level=2>

# Read Image Info

# <codecell>

from PIL import Image, ImageDraw
import numpy as np
import csv as csv

#open image and convert to hsv
im = Image.open("D:\\Dropbox\\ankur\\newspaper\\test2.png")

if im.mode != "L" :
    im2 = im.convert(mode = "L") 

nx,ny =  im2.size
#whitePixel = []
blackPixel = []

i = 1
#chech the pixels
for y in range(ny):
    whiteCount = 0
    blackCount = 0
    for x in range(nx):
        xy = (x,y)
        pix = im2.getpixel(xy)
        if pix == 255: #255 is for white
            #whitePixel.append(xy)
            whiteCount += 1
            #im2.putpixel(xy,1) #used to crudely invert the image
        else :
            blackCount += 1
            #blackPixel.append(xy)
    if blackCount >= (0.05 *nx):
        blackPixel.append((i,y,blackCount))
        i = i +1

file = csv.writer(open("D:\\Dropbox\\ankur\\newspaper\\test2.csv","wb"))

for each in blackPixel:
    file.writerow(each)

# <headingcell level=2>

# Alternate method for findind dark pixels

# <codecell>

import numpy as np
import csv as csv
from operator import itemgetter

file = csv.reader(open("D:\\Dropbox\\ankur\\newspaper\\test2.csv","rb"))
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

i = 0
while i < size :
    low = downIndex[i]-1
    high = int(upIndex[i])+1
    g = []
    k = []
    #print (low,high)
    g = data[low:high]
    #print g
    #k = sorted(g, key=lambda g:g[2]) # method a
    item = ['0', '0', '0'] #random
    k=0
    #print g
    num = low
    '''
    while num < high:
        if int(k) < g[num][2]:
            item = g[num]
            k = g[num][2]
            print item
        num += 1
    '''
    for row in g:
        if (int(k) < int(row[2])):
            item = row
            k = row[2]
    
    #print item #method b
    
    #k = max(g, key =itemgetter(2)) #method c
    i += 1
    dark.append(item)
    
#print dark
#write dark-line y-coordinates and pixelcount to a file
file2 = csv.writer(open("D:\\Dropbox\\ankur\\newspaper\\test2_blackPixels.csv","wb"))
for each in dark:
    file2.writerow(each)
    #print each

# <headingcell level=2>

# WhiteWash

# <codecell>

from PIL import Image, ImageDraw
import numpy as np
import csv as csv

#open dark-line coordinates
file = csv.reader(open("D:\\Dropbox\\ankur\\newspaper\\test2_blackPixels.csv","rb"))
data = []
for row in file:
    data.append(row[1])
#print data

#open image and convert to hsv
im = Image.open("D:\\Dropbox\\ankur\\newspaper\\test2.png")
im2 = im.convert(mode = "L")

line_color = 255
nx,ny =  im2.size
count = 0
for y in data:
    k = int(y)
    for x in range(nx):
        xy = (x,k)
        im2.putpixel(xy,line_color)
        #im2.putpixel((x,int(k)+1),line_color)
        #im2.putpixel((x,int(k)+2),line_color)
        #im2.putpixel((x,int(k)+3),line_color)
        #im2.putpixel((x,int(k)+4),line_color)
        #im2.putpixel((x,int(k)+5),line_color)
        #im2.putpixel((x,int(k)-5),line_color)
        #im2.putpixel((x,int(k)-4),line_color)
        #im2.putpixel((x,int(k)-3),line_color)
        #im2.putpixel((x,int(k)-2),line_color)
        #im2.putpixel((x,int(k)-1),line_color) #padding
        
im2.save("D:\\Dropbox\\ankur\\newspaper\\test2_WhiteWashed.png")
#im2.show()

# <codecell>


