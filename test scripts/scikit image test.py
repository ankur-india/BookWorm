# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Scikit Image Test

# <codecell>

import numpy as np
from skimage import io, color
from skimage.filter import canny, sobel
import matplotlib.pyplot as plt

#read and convert profiles
imFile = io.imread("D:\\Dropbox\\ankur\\test.tif")
imData = color.rgb2gray(imFile)
edges = canny(imData/1.)
edges2 = sobel(imData)

print ("original rgb size = " + np.str(np.size(imFile)))
print ("original gray size = " + np.str(np.size(imData)))

#plots
plt.figure(figsize=(8,3))

plt.subplot(131)
plt.imshow(imFile)
plt.title('Original rgb')

plt.subplot(132)
plt.imshow(edges)
plt.title('canny')

plt.subplot(133)
plt.imshow(edges2)
plt.title('sobel')

plt.show()

