import cv2
import os 
#wepcam
cap =cv2.VideoCapture(0)
fileName="media"
codec=cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)
save_path=f"media"
frame_count = 0

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)#tersdondu
    cv2.imshow("webcam",frame)
    if cv2.waitKey(24) & 0xFF ==ord("k"):
        fileName=os.path.join(save_path,f"frame_{frame_count}.png")
        cv2.imwrite(fileName,frame)
        frame_count += 1
    elif cv2.waitKey(24) & 0xFF ==ord("q"):
        break   

cap.release()

cv2.destroyAllWindows()