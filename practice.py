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
plt.hist(brain_image[:,:,0], bins=10)
#show the histogram
plt.show()
#gaussian filter sigma 5
filter_5=ndimage.gaussian_filter(brain_image,sigma=5)
#draw the image
plt.imshow(filter_5)
#show the image
plt.show()
#histogram of filter sigma 5
plt.hist(filter_5[:,:,0])
#show the histogram
plt.show()
