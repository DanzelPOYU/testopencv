import cv2 
import numpy as np 
#mouse callback function
def draw_circle(event,x,y,flags,param): 
	if event==cv2.EVENT_LBUTTONDBLCLK: 
		cv2.circle(img,(x,y),100,(255,0,0),-1)  

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1): #如果滑鼠事件發生就會跳回setMouseCallback，然後再繼續刷新image
	cv2.imshow('image',img) 
	if cv2.waitKey(20)&0xFF==27: 
		break 
# cv2.imshow('image',img)#因為只有show一次就停下來了
# cv2.waitKey(0)
cv2.destroyAllWindows()