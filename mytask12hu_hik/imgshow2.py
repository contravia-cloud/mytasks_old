import numpy as np

image = np.empty((1280,960), np.uint16)
image.data[:] = open('AfterConvert_RGB.raw').read()

import cv2
cv2.imshow('test', image)
cv2.waitKey()
cv2.destroyAllWindows

