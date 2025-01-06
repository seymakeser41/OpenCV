#for
"""
numbers=[1,2,3,4,5]
for num in numbers: #for döngüsü ile dizinin elemanları kolayca yazdırılır
    print(num)

names=['cınar','seyma','sena']
for name in names:
    print(' my name is {name}')

name='seyma'
for n in name:# string ifade bir dizi gibi harfleri yazdırılabilir
    print(n)

tuple=[((1,2),(3,4),(5,6))] #ikili elemanlar tek tek yazdırılır
for a,b in tuple:
    print(a,b)
d={'k1':1, 'k2':2,'k3':3}
for key,value in d.items():#elemanlar iki şekilde eşleştirilir ve ekrana yazdırılır
    print(key,value)

#FOR UYGULAMALAR 
sayilar=[1,3,5,7,9,12,19,21]
sehirler=['kocaeli','istanbul','ankara','izmir','rize']
urunler= [
    {'name':'samsungs6', 'price':'3000'},
    {'name':'samsungs7', 'price':'4000'},
    {'name':'samsungs8', 'price':'5000'},
    {'name':'samsungs9', 'price':'6000'},
    {'name':'samsungs10', 'price':'7000'}
]
#1-sayılar listesinde hangi sayılar 3ün katıdır
for i in sayilar:
    if i%3==0:
        print( i)
#2 - sayılar listesindeki sayıların toplamı kaçtır
toplam=0
for i in sayilar:
     toplam +=i
print(toplam)

#3-sayilar listesindeki tek sayıların karesini alınız 
for i in sayilar:
    if(i%2==1):
        print(i**2)

#4-şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if len(sehir)<=5:
        print(sehir)

#5-ürünlerin toplamı nedir
toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat
print(toplam)

#6 -ürünlerin fiyatı en fazla 5000 olan ürünleri göster
for urun in urunler:
    if (urun['price'])<=5000:
        print(urun['name'])

#WHİLE 
#1-100e kadar yazdırma
x=1
while x<100: # while döngüsündeki koşul sağlandıkça çalışır fakat değeri değiştirmeyi unutma
    print(x)
    x+=1
print('bitti')

#1-100e çift sayılar
while x<100:
    if x%2==0:
        print(x)
    x+=1

#1-100e tek sayilar
while x<100:
    if x%2==1:
        print(x)
    x+=1
name='' #boşluk olduğu için false değerindedir 
while not name.strip() : #strip fonk ile boşluk girilen bir değer olarak görülmekten çıkar
    name=input('isminizi girin:')
print('merhaba, {name}')

#WHİLE UYGULAMALAR
sayilar=[1,3,5,7,9,12,19,21]
#1-sayılar listesini while ile ekrana yazdırın
a=len(sayilar)
x=0
while x<a:
    print(sayilar[x])
    x+=1

#2-başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdırın
a=int(input('başlangic değeri giriniz:'))
b=int(input('bitiş değeri giriniz:'))
while a<b:
    if a%2==1:
        print(a)
    a+=1


#3-1-100 arasındaki sayıları azalan şekilde yazdırın
x=100
while x>0:
    print(x)
    x-=1

#4-kullanıcıdan aldığınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
numbers=[]
i=0
while i<5:
    sayi=int(input('bir sayi giriniz:'))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)

#5-kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız 
# **ürün sayısını kullanıcıya sorun
# **dictionary listesi yapısı(name ,price) şelkinde olsun
#ürün ekleme işlemi bitince ürünleri ekrana while ile yazdırın
urunler=[]
adet=int(input('kac adet ürün eklemek istiyorsun'))
i=0
while i<adet:
    name=input('ürünün adini giriniz')
    price=input('ürünün fiyatiini giriniz')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f'ürün adi:{urun["name"]} ürün fiyati:{urun["price"]}')

 #BREAK VE CONTİNUE  
name='seyma'
for letter in name :
    if letter=='y':# y harfini görünce döngüyü durdurur
        break
    print(letter)

for letter in name :
    if letter=='y':# y harfini görünce döngüyü atlar sonra devam eder
        continue
    print(letter)

x=0
while x<5:
    if x==2:#2 ye gelince durur
        break
    print(x)

#1- 100e kadar tek sayıların toplamı
x=1
toplam=0
while x<100:
    if x%2==0:
        continue
    toplam+=x
    x+=1
print(toplam)

 #DÖNGÜ METODLARI 
#range
for item in range(2,10,1):# başlangıç ve bitiş değeri arasındaki elemanları artış miktarına göre yazdırır
    print(item)
print(list(range(50,100,20))) #range ile aldığımız değerleri listeye çevirdik
#enumarate
greeting='hello'
for index,letter in enumerate(greeting):#enumarate fonk ile değerleri indeks numaralarına ayırdık
    print(f'index: {index} letter:{letter}')
#zip
list1=[1,2,3,4,5]
list2=['a','b','c','d','e'] #zip methodu ile iki liste eşleşir
print(list(zip(list1,list2)))
for item in zip(list1,list2):
    print(item)

 #comprehensions
numbers=[x*x for x in range(10) if x%3==0] #1 den ona kadarki sayıların karelerinin 3ün katı olanlarını kolayca yazdık
print(numbers)
result=[x if x%2==0 else 'tek' for x in range(1,10)]
print(result)
result=[]
for x in range(3):# iç içe iki döngüyle liste oluşturduk
    for y in range(3):
        result.append((x,y))
print(result)
numbers=[(x,y) for x in range(3) for y in range(3)] #aynı işlemi bu şekilde de yaparız
print(numbers)
 """
 #SAYI TAHMİN OYUNU UYGULAMA
"""
1-100 ARASINDA RASTGELE ÜRETİLECEL BİR SAYI AŞAĞI YUKARI İFADELERİ İLE BULDURMAYA ÇALIŞ
**random modülü içim 'python random' şeklinde arama yapın(hak 5) 
**100 üzerinden puanlama yapın . her soru 20 puan 10 ar azalt
**hak bilgiisni kullanıcıdan al ,can hesapla 

import random
sayi=random.randint(1,100)
hak=5
puan=100
tahmin=0
a=int(input(f'hakkiniz:{hak} tahmininizi girin:'))
while hak>0:
   #a=int(input(f'hakkiniz:{hak} tahmininizi girin:'))
   if a!=sayi:
      hak-=1
      puan-=10
      tahmin+=1
      if a>sayi:
        print('aşaği')
      else:
        print('yukari')
      if hak==0:
        print(f'hakkiniz bitti, puaniiniz: {puan}')
        break
      a=int(input(f'hakkiniz:{hak} {tahmin}. tahmininiz başarisiz , puaniniz{puan} yeni tahmininizi girin:')) 
   else:
       puan+=20
       hak=0
       print(f' {tahmin}. tahmininiz başarili , puaniniz{puan}' )
 """
 #UYGULAMA
 #GİRİLEN BİR SAYİNİN ASAL OLUP OLMADIĞINI BULUN
a=int(input('sayi giriniz:'))
b=int(a/2)
i=2
while i<=b:
    if a%i==0:
       print('sayi asal değil')
       i+=1
       break
    else:
       print('sayi asal')
       break    
if a<2:
    print(' en kücük asal sayi 2 dir')
