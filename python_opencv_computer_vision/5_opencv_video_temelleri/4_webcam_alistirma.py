import cv2

#1- opencv kullanarak webcam üzerinden anlık video kaydı üzerinde çizim işlemi 
#Sırasıyla işlemler:
# *Mouse callback fonksiyonu ile draw_circle fonksiyonu cağırılacak
# * İki adet event oluşturulacak (cv2.EVENT_LBUTTONDOWN ve cv2.EVENT_LBUTTONUP)
# *boolen formatında click olaylarını tutacak değişkenler
# * çizilecek dairelerin ortasını tutacak tuple 
# * x,y, koordinatlarına göre daire çizimi

def draw_circle(event, x, y, flags, param):
    global center, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center=(x,y)
        clicked=False

    if event==cv2.EVENT_LBUTTONUP:
        clicked=True
        


center=(0,0) 
clicked=False


cap=cv2.VideoCapture(0)
cv2.namedWindow('test')
cv2.setMouseCallback('test', draw_circle)

while True:
    ret, frame= cap.read()
    frame= cv2.flip(frame, 1)

    if clicked==True:
        cv2.circle(frame, center, 50,(0,0,255),5)

    cv2.imshow('test',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

