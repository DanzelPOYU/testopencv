import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('test.png',0)

print(img)
# cv2.namedWindow('test',cv2.WINDOW_NORMAL)
# cv2.imshow('test',img)
# cv2.imwrite('test1.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()