#importing matplotlib
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing npimage
from scipy import ndimage
#reading the image
brain_image=plt.imread("BrainNew.jpg")
#print the dimensions
print (brain_image.shape)
#drwaing the image
plt.imshow(brain_image,cmap='Greys_r')
#display
plt.show()
#histogram of brain_image
plt.hist(brain_image, bins=10)
#show the histogram
plt.show()
#gaussian filter sigma 50
filter_50=ndimage.gaussian_filter(brain_image,sigma=50)
#draw the image
plt.imshow(filter_50, cmap='Greys_r')
#show the image
plt.show()
#histogram of filter sigma 40
plt.hist(filter_50, bins=10)
#show the histogram
plt.show()
