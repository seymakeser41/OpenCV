import cv2

#boyutlandır
img=cv2.imread(r"C:\Users\seyma\Desktop\media\aircraft.jpg")
imgResized=cv2.resize(img,(150,150))

#kırp
imgCropped=img[:200, :300]


cv2.imshow("resim", img)
cv2.imshow("boyutlandirilmis", imgResized)
cv2.imshow("kirpilmis", imgCropped)



cv2.waitKey(0)
cv2.destroyAllWindows()