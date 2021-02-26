#importing matplotlib
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing npimage
from scipy import ndimage
#reading the image
brain_image=plt.imread("Brain.jpg")
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
#gaussian filter sigma 40
filter_40=ndimage.gaussian_filter(brain_image,sigma=40)
#draw the image
plt.imshow(filter_40, cmap='Greys_r')
#show the image
plt.show()
#histogram of filter sigma 40
plt.hist(filter_40, bins=10)
#show the histogram
plt.show()
