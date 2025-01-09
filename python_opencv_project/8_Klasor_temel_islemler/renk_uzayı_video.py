import cv2

cap=cv2.VideoCapture(r"media/video1.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret ==False:#ret false döndürdüğü için son değerde hata verbilir o yüzden koşula bu durumu önleriz
        break

    #tek tek frameler seçip dönüştürücez ve döngü q ya basana kadar devam edecek
    cv2.imshow("video",frame)
    if cv2.waitKey(15)&0xFF== ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
