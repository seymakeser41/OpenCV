import cv2
import matplotlib.pyplot as plt

# içe aktar 
einstein = cv2.imread(r"C:\Users\seyma\Desktop\media\einstein.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")

# sınıflandırıcı
face_cascade = cv2.CascadeClassifier(r"C:\Users\seyma\Desktop\opencv_bolumu\cascade\frontalface.xml.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y),(x+w, y+h),(255,255,255),10)
plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")

# barce
# içe aktar 
barce = cv2.imread(r"C:\Users\seyma\Desktop\media\barcelona.jpg", 0)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")

face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 7)


for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y),(x+w, y+h),(255,255,255),10)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")

plt.show()
# kameradan tespit
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
            
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y),(x+w, y+h),(255,255,255),10)
        cv2.imshow("face detect", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()