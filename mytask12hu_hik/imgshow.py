import numpy as np
import cv2
import copy
fd = open('/home/contraviau/python/myproject/mytasks/mytask12hu_hik/img/AfterConvert_RGB.raw', 'rb')
rows = 640 #960
cols = 1280+640 #1280

f = np.fromfile(fd, dtype = np.uint16, count=rows*cols)

fd.close()
im = f.reshape((rows, cols))
im = cv2.resize(im, dsize = (960, 640), interpolation= cv2.INTER_AREA)

# im2 = copy.deepcopy(im[0:1,0:1280])
#
# for i in range(0,20):
#     print(i)
#     img_aad = copy.deepcopy(im[i: (i+1), 0:1280])
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))
#     im2 = np.vstack((im2, img_aad))

# print(np.amax(im))
# print(np.amin(im))
# print(im)

cv2.imshow('test', im)
cv2.waitKey()
cv2.destroyAllWindows

