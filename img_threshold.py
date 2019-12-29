import cv2
import numpy as np 
path='C:/Users/ankush/Desktop/ronaldo.jpg'
img=cv2.imread(path,0)

threshold=150
(t_value,binary)=cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)

cv2.imshow('binary',binary)
cv2.waitKey()
cv2.destroyAllWindows()