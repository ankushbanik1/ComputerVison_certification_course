import cv2
import numpy as np 
path='C:/Users/ankush/Desktop/ronaldo.jpg'
img=cv2.imread(path)

cols=img.shape[1]
row=img.shape[0]
angle=90

center=(cols/2,row/2)

m=cv2.getRotationMatrix2D(center,angle,1)
shifted=cv2.warpAffine(img,m,(cols,row))
cv2.imshow('shifted',shifted)
cv2.waitKey()
cv2.destroyAllWindows()