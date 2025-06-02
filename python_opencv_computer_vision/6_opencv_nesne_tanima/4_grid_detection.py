import cv2
import numpy as np
import matplotlib.pyplot as plt

img_chess=cv2.imread(r"C:\Users\seyma\Desktop\media\satranc.jpg")
img_grid=cv2.imread(r"C:\Users\seyma\Desktop\media\grid.jpg")

#bu fonksiyon 7*7 den 49 tane corner bulr ve bunları corners değişkeninde saklar(49*1 bir dizi)
found,corners= cv2.findChessboardCorners(img_chess, (7,7))
#found değişkeni fonksiyonun corners bulup bulmadığını kontrol etmemmize yarar
if found:
    print('opencv corner buldu')
else:
    print('opencv corner bulamadi')
#bu fonksiyonla bulduğumuz cornerlar çizilir , satırlar arası cornerların ilişkisi de bir çizgiyle bağlanır 
chess=img_chess.copy()
cv2.drawChessboardCorners(chess, (7,7), corners, found)

#aynı işlemleri grid resmi için uyguluyoruz
found1, corners1=cv2.findCirclesGrid(img_grid, (8,11),cv2.CALIB_CB_SYMMETRIC_GRID )

if found1:
    print('corners bulundu')
else:
    print('corners bulunamadı')

grid=img_grid.copy()
cv2.drawChessboardCorners(grid, (8,11), corners1, found)

#görselleştirmeler
cv2.imshow('chess', img_chess)
cv2.imshow('grid', img_grid)
cv2.imshow('corners', chess)
cv2.imshow('corners1', grid)
cv2.waitKey(0)
cv2.destroyAllWindows()