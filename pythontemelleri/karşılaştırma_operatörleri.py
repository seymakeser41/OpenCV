#KARŞILAŞTIRMA OPERATÖRLERİ
"""
a,b,c,d=5,5,10,4
password='1234'
username='seymakeser'
result=a==b #true eşit mi diye karşılaştırma operatörüyle kontrol ettik ve bir sonuç alduk 
result2='sdktrn'==username #false 
result3=a!=b #false eşit değil mi diye karşılaştırdık
result=a > b # büyük mü diye karşılaştırdık 
result=a < b # küçük mü diye karşılaştırdık 
result=a >= b # büyük eşit mi diye karşılaştırdık 
result=a <= b # küçük eşit mi diye karşılaştırdık 
result=True==1 #doğrudur çümkü nümerik olarak bakar

#KARŞILAŞTIRMA ÖPERATÖRLERİ UYGULAMA
#1-Girilen 2 sayıdan hangisi büyüktür?
a=int(input('a'))
b=int(input('b'))
result=a>b
print(f'a:{a} b: {b} den büyüktür: {result}')
#2 - Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız . eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız
vize1=float(input('vize1 notu:'))
vize2=float(input('vize2 notu:'))
final=float(input('final notu:'))
ort= ((((vize1+vize2)/2)*60)/100)+(final*40/100)
print(f'not ortalamanız:{ort} ve dersten geçme durumunuz:{ort>=50}')

x=5
hak=5
devam='e'
result=5 < x < 10 #iki karşılaştırmanın doğruluğuna baktık 
#and
result=x>5 and x<10 #iki karşılaştırmayı yaptık ama and kullandık ikisini de sağlamalı
result=(hak>0) and (devam=='e') #yine iki karşılaştırma doğruysa devam eder

#or
result=(x>0) or (x%2==0) #iki karşılaştırmanın bir tarafının doğruluğu yeterlidir 

#not 
result=not(x>0) #alacağım sonuç tam tersine döner 

#x, 5-10 arasında olan bir çift sayı mı?
result=(x>5 and x<10 ) and x%2==0
print(result)

#OPERATÖRLERLE İLGİLİ UYGULAMA 
#1- Girilwn bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a=int(input('a:'))
result=0<a<100
print(result)
#2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
a=int(input('a:'))
result=0<a and a%2==0
print(result)
#3- email ve parola bilgileri ile giriş kontrolü yapınız
email=seyma@gmail.com
parola=1234
a=str(input('mailiniz:'))
b=int(input('parola:'))
result=a==email and b==parola
print("giriş yapabilme durumunuz:"+ result)

#4- girilen 3 sayıyı büyüklük olarak karşılaştırınız
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
result1=a<b
result2=b<c
result3=c<a
result4=result1==True and 
print(result)
#5-kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayınız 
#  eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın 
#  a-ortalama 50 olsa bile final notu en az 50 olmalıdır 
#  b-finalden 70 alındığında ortalamanın önemi kalmasın
vize1=float(input('vize1 notu:'))
vize2=float(input('vize2 notu:'))
final=float(input('final notu:'))
ort= ((((vize1+vize2)/2)*60)/100)+(final*40/100)
print(f'not ortalamanız:{ort} ve dersten geçme durumunuz:{ort>=50}')

#6-kişinin ad , kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#  formül:(kilo /boy uzunluğunun karesi)
#  aşağıdaki tabloya göre kişi hangi gruba girmektedir 
#  0-18.4 => zayıf 
#  18.4-24.9 =>normal
#  25.0-29.9 => fazla kilolu
#  30.0-34.9 => şişman (obez)
ad=str(input('adiniz:'))
kilo=int(input('kilonuz:'))
boy=float(input('boyunuz:'))
indeks=kilo/(boy**2)
result1=0<indeks<18.5
result2=18.5<=indeks<25
result3=25<=indeks<30
result4=30<=indeks<35
print("zayif olma durumunuz:",  result1)
print("normal olma durumunuz:", result2)
print("fazla kilolu olma durumunuz:", result3)
print("şişman olma durumunuz:", result4)
"""
#İDENTİTY OPERATÖR(İS) VE MEMBERSHİP OPERATÖR(İN)
#İS
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y) # adres ,referans olarak karşılaştırma yapar ve true değerini verir
print(x is z)# adres ,referans olarak karşılaştırma yapar ve false değerini verir
x=[1,2,3]
y=[2,4]
del x[2]
y[1]=1
y.reverse()
print(x==y)# true çümkü değerler aynı oldu 
print(x is y)# false çünkü referanslar farklı
#İN
x=['apple','banana']
print('banana' in x) #true çünkü bu ifade listede var
name='cinar'
print('a' in name) # true a ifadesi namede bulunur
print('a' not in name)# false a ifadesi namede bulunur