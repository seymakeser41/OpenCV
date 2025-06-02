import cv2
import numpy as np
import matplotlib.pyplot as plt
#bilgisayarın kamerasını bu fonksiyonla aktif ederiz
cap=cv2.VideoCapture(0)
# alınan videnun boyutlarını bu fonksiyonlarla öğrenebiliriz
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#videodaki her frameyi alıp gray formatta görüntüledik
while True:
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release() #videoyu serbest bıraktık
cv2.destroyAllWindows()