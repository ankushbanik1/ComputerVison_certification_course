import cv2
import numpy
path='C:/Users/ankush/Pictures/Exported Videos/weekend.mp4'
cap=cv2.VideoCapture(path)

fource=cv2.VideoWriter_fourcc(*'XVID')
fps=30
frameSize=(720,480)
out=cv2.VideoWriter('sample.avi',fource,fps,frameSize)
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('vid',frame)
    if cv2.waitKey(1)& 0XFF ==ord('q'):
        break
cap.release()

cv2.destroyAllWindows()