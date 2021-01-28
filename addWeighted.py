import cv2
import numpy as np
img=cv2.imread('test.png')

img1=img[200:300,100:300]
img2=img[100:200,300:500]

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)

img[100:200,300:500]=dst

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindow()