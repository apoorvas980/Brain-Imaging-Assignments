#importing matplotlib
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing npimage
from scipy import ndimage
#reading the image
brain_image=plt.imread("brain.jpg")
#print the dimensions
print (brain_image.shape)
#drwaing the image
plt.imshow(brain_image,cmap='Greys_r')
#display
plt.show()
#histogram of brain_image
plt.hist(brain_image[:,:,0], bins=10)
