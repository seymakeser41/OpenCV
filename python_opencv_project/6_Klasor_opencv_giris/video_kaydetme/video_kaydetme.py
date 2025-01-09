from encodings.johab import codec
from fileinput import filename

import cv2
#wepcam
cap =cv2.VideoCapture(0)
fileName="media"
codec=cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)

videoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)#tersdondu
    videoFileOutput.write(frame)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(24) & 0xFF ==ord("q"):
        break

videoFileOutput.release()
cap.release()

cv2.destroyAllWindows()