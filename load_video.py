import cv2
import numpy
path='C:/Users/ankush/Pictures/Exported Videos/weekend.mp4'
cap=cv2.VideoCapture(path)

while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('vid',frame)
    if cv2.waitKey(1)& 0XFF ==ord('q'):
        break
cap.release()

cv2.destroyAllWindows()