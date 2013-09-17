from PIL import Image, ImageDraw
import csv as csv
import sys
import os

def read_info(location , imFile) :
    #open image and convert to hsv if needed
    
    im = Image.open(location + imFile)
    if im.mode != "L" :
        im2 = im.convert(mode = "L") 
    else:
        im2 = im
    #print im2.mode
    
    nx,ny =  im2.size
    #whitePixel = []
    blackPixel = []
    
    i = 1
    #check the pixels
    for y in range(ny):
        whiteCount = 0
        blackCount = 0
        for x in range(nx):
            xy = (x,y)
            pix = im2.getpixel(xy)
            if pix == 255: #255 is for white
                #whitePixel.append(xy)
                whiteCount += 1
                #im2.putpixel(xy,1) #used to crudely invert the image - required for testing purposes
            else :
                blackCount += 1
                #blackPixel.append(xy)
        if blackCount >= (0.05 *nx):
            blackPixel.append((i,y,blackCount))
            i = i +1
    
    file = csv.writer(open(location + "test.csv","wb"))
    
    for each in blackPixel:
        file.writerow(each)


if __name__ == '__main__':
    
    #default location
    location  = "D:\\Dropbox\\ankur\\pixel_tests\\"  #file location
    imFile = "test.png"
    
    #user input for location
    #if(len(sys.argv)!=5):
    #    print "Usage: python read_image_info.py -location <location> -imFile <file name>"
    #    print "Error : insufficient arguments"
    #    exit()
    #
    #if(sys.argv[1]=="-location"):
    #    location=sys.argv[2]
    #else:
    #    print "Usage: python read_image_info.py -location <location> -imFile <file name>"
    #    print "Error : wrong location"
    #    exit()
    #
    #if(sys.argv[3]=="-imFile"):
    #    imFile=sys.argv[4]
    #else:
    #    print "Usage: python read_image_info.py -location <location> -imFile <file name>"
    #    print "Error : wrong filename"
    #    exit()
    
    read_info(location,imFile)
