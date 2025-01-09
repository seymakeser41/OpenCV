import cv2
cv2.namedWindow("image")
img=cv2.imread(r"media/kus_resmi.jpg")
img=cv2.resize(img,(600,400))
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()