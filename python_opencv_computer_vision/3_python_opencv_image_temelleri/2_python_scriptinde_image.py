import cv2
#resmi bir pencerede gösterip esc ye basınca kapanacak olarak ayarladık
img=cv2.imread(r"C:\Users\seyma\Desktop\media\kus_resmi.jpg")
while True:

   cv2.imshow('resim',img)

   if cv2.waitKey(0) & 0xFF ==27 :
      break
   
cv2.destroyAllWindows()
