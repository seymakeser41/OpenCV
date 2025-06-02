import numpy as np
mylist=[1,2,3,4] #liste oluşturma 
print(type(mylist)) #tipini öğrenme
myarray=np.array(list)#arraye dönüştürme
otoarray=np.arange(0,10,2) #otomatik array oluşturma başlangıç , son ve artış(default=1)
sifirarray=np.zeros(shape=(5,5)) # 5 satır ve 5 sütündan oluşan elemanlarının her biri float olarak 0 olan bir dizi tanımlar
birarray=np.ones(shape=(4,3)) #4 satır ve 3 sütundan oluşan her elemanı float 1 den oluşan bir dizi
randomarray=np.random.randint(0,100,10)#başlangıç ,son ve kaç eleman olacağı bilgisiyle random dizi oluşturur
min=randomarray.min()#dizideki min değer
max=randomarray.max()#dizideki maz değer
wheremax=randomarray.argmax()#max değer dizinin kaçıncı indisinde
wheremin=randomarray.argmin()#min değer dizinin kaçıncı indisinde
ortalama=randomarray.mean()#dizideki elemanların ortalaması
boyut=randomarray.shape #dizide kaç eleman var
newshape=randomarray.reshape((2,5)) #diziyi 2 satır 5 sütün olarak boyutlandırdık
array2=np.arange(0,100).reshape((10,10)) #10 satır 10 sütünluk ve birer artarak 100e kadar otomatik doldurur
sütün1=array2[:,1].reshape(10,1)#sadece 1. sütün elemanlrını alır ve boyutunu 10 satır 1 sütün olarak değiştirir
satir5=array2[5,:] #sadece 5 satırdaki elemanları alır
satir2sutün2=array2[0:2,0:2] #2.satır ve 2. sütüna kadar olan elemanlar
copyarray=array2.copy() #arrayi kopyalama
