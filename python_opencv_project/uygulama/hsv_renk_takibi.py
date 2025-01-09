import cv2
import numpy as np

cap =cv2.VideoCapture(0)
def nothing(x):
    pass

cv2.namedWindow("settings")
cv2.createTrackbar("lower-hue", "settings",0,180,nothing)
cv2.createTrackbar("lower-saturation", "settings",0,255,nothing)
cv2.createTrackbar("lower-value", "settings",0,255,nothing)
cv2.createTrackbar("upper-hue", "settings",0,180,nothing)
cv2.createTrackbar("upper-saturation", "settings",0,255,nothing)
cv2.createTrackbar("upper-value", "settings",0,255,nothing)

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    
    lh=cv2.getTrackbarPos("lower-hue","settings")
    ls=cv2.getTrackbarPos("lower-saturation","settings")
    lv=cv2.getTrackbarPos("lower-value","settings")
    uh=cv2.getTrackbarPos("upper-hue","settings")
    us=cv2.getTrackbarPos("upper-saturation","settings")
    uv=cv2.getTrackbarPos("upper-value","settings")

    lower_color=np.array([lh,ls,lv]) 
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Tracked Object", bitwise)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()