"""
---ArUco markörleri oluşturma:
 ArUco işaretçileri, bilgisayarlarla görme algoritmalarının kolayca algılayabileceği 2B ikili desenlerdir.
1. kullanmak için ArUco sözlüğünü seçin
2. hangi ArUco ID'sini çizeceğinizi belirtin .
3. çıktı ArUco görntünüz için bellek ayırın(piksel cinsinden)
4. ArUco etiketini çizmek içinişlevi ullanın (drawMarkers)
5. ArUco işaretçisinin kendisini çizin 

Olec kalacev kullanarak hazır ArUco marörü kullanılabilir.

ÖRNEK: cv2.aruco.DICT_N*N_M (N*N Boyutta M kadar sözlükle oluşturulabilecek benzersiz ArUco kimliğini temsil eder )


--- ArUco işaretleyicilerini algılama :(geçek zamanı video akışlarında)
1. ArUco sözlğünü belirleme  cv2.aruco.Dictionary_get
2. ArUco dedektörüne parametlerelerin oluşturulması  v2.aruco.DetectorParameters_create
3. işaretçileri cv2.aruco.detectMarkers ile algılanması 
"""
# gerekli paketleri içeri aktar
import argparse
import imutils
import cv2
import sys

# Argüman ayrıştırıcısını oluşturun ve argümanları ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image containing ArUCo tag")
ap.add_argument("-t", "--type", type=str,default="DICT_ARUCO_ORIGINAL",help="type of ArUCo tag to detect")
args = vars(ap.parse_args())

# OpenCV'nin desteklediği her olası ArUco etiketinin adlarını tanımlayın
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# resmi yükle ve boyutlandır 
print("[INFO] loading image...")
image = cv2.imread(args["image"])


image = imutils.resize(image, width=600)
# OpenCV tarafından desteklenen her ArUCo etiketinin var olduğunu doğrulayın
if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(args["type"]))
	sys.exit(0)
# ArUCo sözlüğünü yükleyin, ArUCo parametrelerini alın ve işaretçileri tespit edin
print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,parameters=arucoParams)


# *en az* bir ArUco işaretçisinin algılandığında yapılacak işlemler
if len(corners) > 0:
    # Algılanan işaretçileri otomatik olarak çiz
    cv2.aruco.drawDetectedMarkers(image, corners, ids)

    # ArUco kimlikleri listesini düzleştirin
    ids = ids.flatten()

    # algılanan ArUCo köşeleri üzerinde döngü kurun
    for (markerCorner, markerID) in zip(corners, ids):
        # İşaretleyici köşelerini ayıklayın 
        # sol üst, sağ üst, sağ alt ve sol alt sırası)
        corners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = corners

        # (x, y)-koordinat çiftlerinin her birini tamsayılara dönüştürün
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        topLeft = (int(topLeft[0]), int(topLeft[1]))

        # ArUCo algılamasının sınırlayıcı kutusunu çizin
        cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
        cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
        cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
        cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)

        # ArUco işaretleyici'nin merkez (x, y)-koordinatlarını hesaplayın ve çizin
        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
        cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

        # Resmin üzerine ArUco işaretleyici kimliğini yazın
        cv2.putText(image, str(markerID), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        print("[INFO] ArUco marker ID: {}".format(markerID))

        # Çıktıyı görüntüle
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
