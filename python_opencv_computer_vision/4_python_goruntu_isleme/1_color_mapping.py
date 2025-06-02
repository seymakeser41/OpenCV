import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\kus_resmi.jpg") #RGB  formatta

img1=cv2.cvtColor(img,cv2.COLOR_RGB2HSV) #HSV format
img2=cv2.cvtColor(img,cv2.COLOR_RGB2HLS_FULL) #HLS formatı 


cv2.imshow('resim',img)
cv2.imshow('resim1',img1)
cv2.imshow('resim2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()