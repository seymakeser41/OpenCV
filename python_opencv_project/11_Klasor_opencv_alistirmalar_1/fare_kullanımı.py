#basılan noktanın çemberin merkezi olduğu çemberler çizilecek
import cv2
cap=cv2.VideoCapture(r"media/line.mp4")

circles=[]#çemberlerin merkezlerini tutmak için dizi tanımladık
def mouse(event,x,y,flags,params):#fareye basıldığında ne iş yapacağını anlatan fonksiyon
    if event==cv2.EVENT_LBUTTONDOWN:#sol tuşa basıldıysa noktayı merkez olarak circles dizisine ekler
        circles.append((x,y))
        
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",mouse)#farenin yaptığı işi alacak fonksiyon

while 1:
    _,frame=cap.read()#frameleri çektik
    frame=cv2.resize(frame,(640,480))#boyutlandırdık
    
    for center in circles:#merkezlere daire çizen fonksiyon 
        cv2.circle(frame,center,20,(255,0,0),-1)
        
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:# esc basınca çıkar
        break
    elif key == ord("h"):# h basınca temizler
        circles=[]
        
cap.release()
cv2.destroyAllWindows()