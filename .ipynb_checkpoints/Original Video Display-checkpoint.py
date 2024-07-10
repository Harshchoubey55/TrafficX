#---------------------------------------------------IMPORTING LIBRARIES-------------------------------------------------------------------------------
import cv2
import numpy as np


#---------------------------------------------------------------------------------------------------------------------------------
cap=cv2.VideoCapture("C:\Users\SAGNIK\Desktop\PBL\Traffic\input.mp4")


while(True):
    ret,frame1=cap.read()
    cv2.imshow("Video Original",frame1)
    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()
cap.release()