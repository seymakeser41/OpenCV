import cv2
#wepcam
cap =cv2.VideoCapture(0)
cap2=cv2.VideoCapture(r"media/video.mp4")
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)#tersdondu
    cv2.imshow("webcam",frame)
    if cv2.waitKey(24) & 0xFF ==ord("q"):
        break

#videocekme
while True:
    ret,frame=cap2.read()
    if ret==0:
        break

    frame=cv2.flip(frame,1)#tersdondu
    cv2.imshow("video",frame)
    if cv2.waitKey(24) & 0xFF ==ord("q"):
        break
cap.release()
cap2.release()
cv2.destroyAllWindows()