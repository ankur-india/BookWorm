from PIL import Image, ImageDraw
import numpy as np
import csv as csv

#open dark-line coordinates
file = csv.reader(open("D:\\Dropbox\\ankur\\pixel_tests\\test_dark_12072013.csv","rb"))	//read information saved by "find_dark_line.py"
data = []
for row in file:
    data.append(row[1])
#print data

#open image and convert to hsv
im = Image.open("D:\\Dropbox\\ankur\\pixel_tests\\test.png")
if im.mode != "L" :
    im2 = im.convert(mode = "L") 
else
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
im2.save("D:\\Dropbox\\ankur\\pixel_tests\\boundary_markers_12072013.png")
im2.show()