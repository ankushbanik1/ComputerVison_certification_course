import cv2
import numpy
path='C:/Users/ankush/Desktop/ronaldo.jpg'

img=cv2.imread(path)

threshold=50
threshold2=100

canny=cv2.Canny(img,threshold,threshold2)
cv2.imshow('canny',canny)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()