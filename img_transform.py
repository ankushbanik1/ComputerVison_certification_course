import cv2
import numpy as np 
path='C:/Users/ankush/Desktop/ronaldo.jpg'
img=cv2.imread(path)

cols=img.shape[1]
row=img.shape[0]

m=np.float32([[1,0,-150],[0,1,-150]])

shifted=cv2.warpAffine(img,m,(cols,row))

cv2.imshow('shifted',shifted)
cv2.waitKey()
cv2.destroyAllWindows()