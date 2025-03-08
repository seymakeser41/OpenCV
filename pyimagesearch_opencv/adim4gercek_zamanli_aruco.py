# Gerekli paketleri içeri aktar
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys

# Argüman ayrıştırıcısını oluşturun ve argümanları ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL",
                help="type of ArUCo tag to detect")
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

# Seçilen ArUco tipi kontrol edilir
if args["type"] not in ARUCO_DICT:
    print("[INFO] ArUCo tag of '{}' is not supported".format(args["type"]))
    sys.exit(0)

# ArUCo sözlüğünü yükleyin, ArUCo parametrelerini alın
print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters()

# Video akışını başlatın ve kamera sensörünün ısınmasını bekleyin
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Tüm framelerde işlem yapmak için döngü kurun
while True:
    # frameleri al ve boyutlandır
    frame = vs.read()
    frame = imutils.resize(frame, width=1000)

    # ArUCo işaretleyicileri algıla
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

    # En az bir ArUco işaretçisi algılandıysa işlem yap
    if len(corners) > 0:
        # ArUco kimlikleri listesini düzleştirin
        ids = ids.flatten()

        # Algılanan ArUCo köşeleri üzerinde döngü kurun
        for (markerCorner, markerID) in zip(corners, ids):
            # İşaretleyici köşelerini ayıklayın 
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            # (x, y)-koordinat çiftlerinin her birini tamsayılara dönüştürün
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            # ArUCo algılamasının sınırlarını çiz
            cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

            # ArUco işaretleyici'nin merkez (x, y)-koordinatlarını hesapla ve çiz
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

            # Resmin üzerine ArUco işaretleyici kimliğini yaz
            cv2.putText(frame, str(markerID),
                        (topLeft[0], topLeft[1] - 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

    # Frameleri'i göster
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # 'q' ya basınca çık
    if key == ord("q"):
        break


cv2.destroyAllWindows()
vs.stop()
