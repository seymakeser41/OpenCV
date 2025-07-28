import cv2
import numpy as np 

# resmi içe aktar 
img = cv2.imread(r"C:\Users\seyma\Desktop\media\aircraft.jpg")
cv2.imshow("Orijinal", img)

# yatay
hor = np.hstack((img,img))
cv2.imshow("Yatay",hor)

# dikey
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)

cv2.waitKey(0)
cv2.destroyAllWindows()