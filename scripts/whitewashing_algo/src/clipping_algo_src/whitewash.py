from PIL import Image, ImageDraw
import numpy as np
import csv as csv

def whitewash(location,matraFile) :
    
    #open dark-line coordinates
    file = csv.reader(open(location + matraFile,"rb"))	#read information saved by "find_dark_line.py"
    data = []
    for row in file:
        data.append(row[1])
    #print data
    
    #open image and convert to hsv
    im = Image.open("D:\\Dropbox\\ankur\\pixel_tests\\test.png") #change this if using user input paths
    if im.mode != "L" :
        im2 = im.convert(mode = "L") 
    else:
        im2 = im
    
    line_color = 255	#color to use for washing over the pixel coordinates
    nx,ny =  im2.size
    count = 0
    for y in data:
        k = int(y)
        for x in range(nx):
            xy = (x,k)
            im2.putpixel(xy,line_color)
            im2.putpixel((x,int(y)+1),line_color)
            im2.putpixel((x,int(y)+2),line_color)
            im2.putpixel((x,int(y)-1),line_color) #padding  #NOTE : limits are to be set manually depending on the document
    '''
            im2.putpixel((x,30),line_color)
            im2.putpixel((x,31),line_color)
            im2.putpixel((x,32),line_color)
            im2.putpixel((x,33),line_color)
    '''									#additional padding, used while testing/debugging
    
    #save the new image file
    im2.save("D:\\Dropbox\\ankur\\pixel_tests\\boundary_markers_12072013.png") #change this if using user input paths 
    im2.show()

if __name__ == '__main__':
    
    #default location
    location  = "D:\\Dropbox\\ankur\\pixel_tests\\"  #file location
    matraFile = "test_dark_12072013.csv"
    
    #user input for location
    #if(len(sys.argv)!=5):
    #    print "Usage: python read_image_info.py -location <location> -matraFile <file name>"
    #    print "Error : insufficient arguments"
    #    exit()
    #
    #if(sys.argv[1]=="-location"):
    #    location=sys.argv[2]
    #else:
    #    print "Usage: python read_image_info.py -location <location> -matraFile <file name>"
    #    print "Error : wrong location"
    #    exit()
    #
    #if(sys.argv[3]=="-matraFile"):
    #    imFile=sys.argv[4]
    #else:
    #    print "Usage: python read_image_info.py -location <location> -matraFile <file name>"
    #    print "Error : wrong filename"
    #    exit()
    
    whitewash(location,matraFile)
