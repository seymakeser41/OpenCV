import cv2
import os
img=cv2.imread(r"media/kus_resmi.jpg",cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
save_path=f"media"
frame=os.path.join(save_path,f"kus_resmi_1.png")
cv2.imwrite(frame,img)

cv2.waitKey(0)
cv2.destroyAllWindows()