# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# PIL and Scikit Image Test

# <headingcell level=1>

# Basic Manipulation tests

# <codecell>

#resize the picture

from PIL import Image

location = "D:\\Dropbox\\ankur\\newspaper\\"
imFile = "test1.png"
im = Image.open(location + imFile)
nx,ny = im.size
img = im.resize((int(nx*10), int(ny*10)), Image.BICUBIC)
#img.show()
img.save(location + imFile+"_resized.png",dpi=(2500,2500))

# <headingcell level=1>

# perform adaptive thresholding

# <codecell>

import Image
from skimage.filter import threshold_adaptive
import numpy as np

location = "D:\\Dropbox\\ankur\\newspaper\\"
imFile = "test1.png_resized.png"
im2 = Image.open(location + imFile)
im = im2.convert(mode = "L")
imData = np.array(im)

block_size = 40
binary_adaptive = threshold_adaptive(imData, block_size, offset=10)
#imshow(binary_adaptive)
imsave(location + imFile + "_denoised.png", binary_adaptive)

# <headingcell level=1>

# perform skeltonize

# <codecell>

import numpy as np
from skimage.morphology import skeletonize

location = "D:\\Dropbox\\ankur\\newspaper\\"
imFile = "test1_new3.png"
im2 = Image.open(location + imFile)

im = im2.convert(mode = "L")
imData = np.array(im)

block_size = 40
binary_adaptive = threshold_adaptive(imData, block_size, offset=10)

skeleton = skeletonize(binary_adaptive)
#imshow(skeleton)
imsave(location + imFile + "_skeleton.png", skeleton)

# <headingcell level=1>

# Reading Pixel information

# <codecell>

from PIL import Image, ImageDraw
import csv as csv

#open image and convert to hsv
location = "D:\\Dropbox\\ankur\\pixel_tests\\"
imFile = "test.png"
im = Image.open(location + imFile)
im2 = im.convert(mode = "L") #TO DO :maybe add a check before conversion

nx,ny =  im2.size
#whitePixel = []
blackPixel = []

i = 1
#chech the pixel colors
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

#write pixel information to file
file = csv.writer(open(location + "test.csv","wb"))

for each in blackPixel:
    file.writerow(each)

# <headingcell level=1>

# Basic Pixel Manipulation - Line Detection

# <codecell>

import csv as csv
from operator import itemgetter # required for "method C"

location = "D:\\Dropbox\\ankur\\pixel_tests\\"
dataFile = "test.csv"
file = csv.reader(open(location + dataFile,"rb"))

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
    if prev == int(row[1]) -1: 
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

for i in range(size):
    low = downIndex[i]
    high = int(upIndex[i])+1
    g = []
    k = []
    g = data[low:high]
    #print g
    #k = sorted(g, key=lambda g:g[2]) # method a
    '''
    k=0
    for row in g:
       if k < row[2]:
            k = row[2]
            item = row
    print item #method b
    '''
    k = max(g, key =itemgetter(2)) #method c
    dark.append(k)
    
#print dark

#write dark-line y-coordinates and pixelcount to a file
file2 = csv.writer(open(location + "test_dark.csv","wb"))
for each in dark:
    file2.writerow(each)

# <headingcell level=1>

# Manipulate the darklines - make white

# <codecell>

from PIL import Image, ImageDraw
import csv as csv

#open dark-line coordinates
location = "D:\\Dropbox\\ankur\\pixel_tests\\"
dataFile = "test_dark.csv"
file = csv.reader(open(location + dataFile,"rb"))

data = []
for row in file:
    data.append(row[1])

#open image and convert to hsv
im = Image.open("D:\\Dropbox\\ankur\\pixel_tests\\test.png")
im2 = im.convert(mode = "L")

nx,ny =  im2.size
count = 0
for y in data:
    k = int(y)
    for x in range(nx):
        xy = (x,k)
        im2.putpixel(xy,0)

#save the new, whitewashed image
im2.save(location + "test_washed.png")
#im2.show()

# <codecell>


