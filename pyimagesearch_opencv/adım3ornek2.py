
#kütüphaneleri import ettik
import argparse
import imutils
import cv2
# argparse ayrıştırıcısını oluşturun ve argümanları ayrışturın
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,help="path to input image")
# args = vars(ap.parse_args())
#image = cv2.imread(args["image"])
image = cv2.imread(r"C:\Users\seyma\Desktop\media\tetris.png") #görüntüyü yükledik
cv2.imshow("Image", image)

#gri formata çevirdik
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

edged = cv2.Canny(gray, 30, 150) #kenarları tespit etti
cv2.imshow("Edged", edged)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1] #threshold işlemi ile gereksiz tonları attı gürültüyü azalttı
cv2.imshow("Thresh", thresh)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #konturları bulduk
cnts = imutils.grab_contours(cnts) #konturları sıraladık
output = image.copy()

for c in cnts: #konturlarda gezip çizim yaptı
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)

text = " resimde {} tane obje buldum".format(len(cnts)) #konturları kullanarak tespit ettiğimiz nesnelerin sayısını yazdı
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
cv2.imshow("Contours", output)

mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)#maske işlemi uyguladık , erozyon ile gürültüyü azalttık
cv2.imshow("Eroded", mask)

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5) #bu işlemle daha da bu bölgeleri ön plana çıkardık
cv2.imshow("Dilated", mask)

mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)#bu işlemle o bölgeyi koruruz
cv2.imshow("Output", output)






cv2.waitKey(0)