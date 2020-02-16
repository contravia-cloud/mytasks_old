import cv2


img = cv2.imread('img/bird.png')#, -1)
img = cv2.resize(img, (224, 224))

img = img.reshape(-1, 224, 224, 3)
cv2.imshow('test', img)
cv2.waitKey()