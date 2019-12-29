import cv2
import numpy as np
path='C:/Users/ankush/Desktop/ronaldo.jpg'
matrix=(7,7)
img=cv2.imread(path)

blur=cv2.GaussianBlur(img,matrix,0)
cv2.imshow('blur',blur)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()