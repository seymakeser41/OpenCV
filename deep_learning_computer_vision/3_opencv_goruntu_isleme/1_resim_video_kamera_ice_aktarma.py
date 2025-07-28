import cv2
import time

#resim içe aktarma 

img=cv2.imread(r"C:\Users\seyma\Desktop\media\aircraft.jpg",0) #gray format
cv2.imshow("resim", img)

#video içeri aktarma 

cap=cv2.VideoCapture(r"C:\Users\seyma\Desktop\media\car.mp4")
print("genişlik:", cap.get(3))
print("yükseklik:", cap.get(4))

if cap.isOpened()==False:
    print("hata")

while True:
    ret,frame=cap.read()
    if ret==True:
       time.sleep(0.01)
       cv2.imshow("video",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF== ord('q'):
         break 

cap.release()
cv2.destroyAllWindows()

#kamera kullanma 

cap2=cv2.VideoCapture(0)

while True:
    ret,frame=cap2.read()
    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) & 0xFF ==('q'): break

cap2.release()
cv2.destroyAllWindows()  

#sadece resim için pencere kapama
if cv2.waitKey(0) & 0xFF ==27:
    cv2.destroyAllWindows()

