import cv2
import time #videonun gösterim hızını ayarlamak için gerekli
#video okundu
cap=cv2.VideoCapture(r"C:\Users\seyma\Desktop\media\dog.mp4")

#video açılmadıysa uyarı verdi ve açıldıysa her bir frami belirtilen hızda gösterdi
if cap.isOpened() ==False:
    print('videoya baglanmadi')
while cap.isOpened():
    ret,frame= cap.read()

    if ret==True:
        cv2.imshow('frame',frame)
        time.sleep(1/30) #1 periyotluk zamanda 25 frame basacak olarak hız ayarlanır

        if cv2.waitKey(20) & 0xFF ==ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()