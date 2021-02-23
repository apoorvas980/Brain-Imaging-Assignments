#importing matplotlib to the environment
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing ndimage from scipy
from scipy import ndimage
#to read the brain image into the numpy ndarray
brain_image=plt.imread("Brain.jpg")
#to find out the dimensions of the image
print (brain_image.shape)
#to draw the brain image
plt.imshow(brain_image, cmap='Greys_r')
#to show the image
plt.show()
#histogram of the image
plt.hist(brain_image)
#to display the histogram
plt.show()
#applying gaussian filter with sigma=30
brain_filter_30=ndimage.gaussian_filter(brain_image,sigma=30)
#draw the filtered image
plt.imshow(brain_filter_30, cmap='Greys_r')
#display the image
plt.show()
#histogram for the filtered image
plt.hist(brain_filter_30)
#display the histogram
plt.show()
