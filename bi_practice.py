conda activate image_processing
python
import matplotlib.pyplot as plt
from scipy import misc, ndimage
face=misc.face()
plt.imshow(face)
plt.show()
