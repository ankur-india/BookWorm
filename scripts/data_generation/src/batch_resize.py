# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Directory parse

# <codecell>

import glob
import Image

def batch_resize(location):
    
    #jpegList = glob.glob(path+"*.jpg")
    #gifList = glob.glob(path+"*.gif")	#to be used if these formats are required, if a GUI is made in the future, should appear as an option
    pngList = glob.glob(location+"*.png")
    
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

if __name__ == '__main__':
    
    #default location
    location  = "D:\\Dropbox\\ankur\\pixel_tests\\"  #file location
    
    #user input for location
    #if(len(sys.argv)!=3):
    #    print "Usage: python read_image_info.py -location <location> "
    #    print "Error : insufficient arguments"
    #    exit()
    #
    #if(sys.argv[1]=="-location"):
    #    location=sys.argv[2]
    #else:
    #    print "Usage: python read_image_info.py -location <location> "
    #    print "Error : wrong location"
    #    exit()
    #
    
    batch_resize(location)

