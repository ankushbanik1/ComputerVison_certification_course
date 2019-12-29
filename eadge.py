import sys

import cv2
import numpy as np 
path='C:/Users/ankush/Desktop/ronaldo.jpg'
img=cv2.imread(path,0)


soble_hori=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
soble_ver=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
canny=cv2.Canny(img,50,240)

cv2.imshow('soble_hori',soble_hori)
cv2.imshow('soble_ver',soble_ver)
cv2.imshow('canny',canny)
cv2.imshow('laplacian',laplacian)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()