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
