# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Directory parse

# <codecell>

import glob
import Image

path = "D:\\Dropbox\\ankur\\BookWorm\\small\\"

#jpegList = glob.glob(path+"*.jpg")
#gifList = glob.glob(path+"*.gif")	#to be used if these formats are required, if a GUI is made in the future, should appear as an option
pngList = glob.glob(path+"*.png")

#print size(pngList)



count = 0
for each in pngList:
    im = Image.open(each)
    nx,ny = im.size
    #print (nx,ny)   
    img = im.resize((int(nx*5), int(ny*5)), Image.BICUBIC)
    name = str(count)
    img.save(each+"_resized_58.png",dpi=(2500,2500))	#default value selected after testing with several images, should be set by user as per requirements
    count += 1

#print count	#used for generating statistics while testing/debugging
    

# <codecell>


