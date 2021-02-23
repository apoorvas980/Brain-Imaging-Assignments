#importing matplotlib to the environment
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing ndimage from scipy
from scipy import ndimage
#to read the brain image into the numpy ndarray
brain_image=plt.imread("Brain.jpg")
#to find out the dimensions of the image
brain_image.shape
