import cv2

windowName="live video"
cv2.namedWindow(windowName)

cap=cv2.VideoCapture(0)

print("width:"+str(cap.get(3)))#cap in 3. değişkeni genişliği tutar
print("height:"+str(cap.get(4)))#yüksekliği aldık

cap.set(3,1280)#bu fonksiyonla çözünürlükleri değiştirdik
cap.set(4,720)

print("new_width:"+str(cap.get(3)))
print("new_height:"+str(cap.get(4)))

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    cv2.imshow(windowName,frame)
    
    if cv2.waitKey(1) == 27:#esc
        break
    
cap.release()
cv2.destroyAllWindows()
