import cv2
import numpy
path='C:/Users/ankush/Desktop/ronaldo.jpg'

img=cv2.imread(path)
dimpixel=7
color=700
space=100
filterr=cv2.bilateralFilter(img,dimpixel,color,space)
cv2.imshow('filter',filterr)
cv2.waitKey()
cv2.destroyAllWindows()