#KOŞUL İFADELERİ
#İF VE ELSE BLOKLARI
"""
if 3>2:
   print('hoş geldin') #koşul sağlandığı için print ifadesi çalışır

username='seyma'
password='123'
if (username=='seyma'):
    if (password=='123'):
      print('hoşgeldiniz')
    else: #if ifadesindeki koşul yanlışsa çalışır doğruysa işlem yapılır
      print('parola yanliş')
else:
   print('username yanliş')


x=int(input('x:'))
y=int(input('y:'))
if x>y:
   print('x yden büyüktür')
elif(x==y): #if ifadesi yanlışsa kontrol edilir ve böyle devam eder
   print('x ye ye eşit')
else:
   print('y xden büyüktür')

num=int(input('sayi:'))
if num>0:
   print('sayı pozitiftir')
elif num<0:
   print('sayı negatiftir')
else:
   print('sayı sıfırdır')

#UYGULAMLAR 1:
#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.
name=str(input('adiniz:'))
yas=int(input('yasiniz:'))
egt=str(input('eğitim durumunuz(ilkokul,ortaokul ,lise,üniversite)'))


if (yas>=18):
   if(egt=='lise' or egt=='üniversite'):
      print('ehliyet alabilirsiniz')
   else:
      print('ehliyet almak icin eğitim durumunuz lise veya üniversite olmalidir')
else:
   print('ehliyet almaniz için en az 18 yaşinda olmalisiniz')
  
#2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığını karşılık gelen not bilgisini yazdırın.
#0-24==0
#25-44==1
#45-54==2
#55-69==3
#70-84==4
#85-100==5

yazizilibir=int(input('birinci yazili notunu giriniz:'))
yaziliiki=int(input('ikinci yazili notunu giriniz:'))
sözlü=int(input('sözlü notunu giriniz:'))
ort=(yazizilibir + yaziliiki + sözlü)/3
if 0<ort<25:
    print('notunuz 0 ')
elif 25<=ort<45:
    print('notunuz 1 ')
elif 45<=ort<55:
    print('notunuz 2 ')
elif 55<=ort<70:
    print('notunuz 3 ')
elif 70<=ort<85:
    print('notunuz 4 ')
else:
    print('notunuz 5 ')

#3-Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#1.bakım==1.yıl
#2.bakım==2.yıl
#3.bakım==3.yıl
#  süre hesabını alınan gün , ay , yıl bilgisine göre gün bazlı hesaplayınız (datetime modülünü kullanarak)
import datetime
tarih=input('araciniz hangi tarihte trafiğe çikti(2019/8/9:)')
tarih=tarih.split('/')
trafikcikiş=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafikcikiş
day=(fark.days)


if day<=365:
    print('1. servis araliği')
elif 365<day<=365*2:
    print('2. servis araliği')
elif 365*2<day<=365*3:
    print('3. servis araliği')
else:
    print('hatali süre')
"""
#UYGULAMA 2:
"""
#1- Girilwn bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a=int(input('sayi giriniz:'))
if a<100:
    print('sayi yüzden küçüktür')
elif a>100:
    print('sayi yüzden büyüktür')
else:
    print('sayi yüzdür')
   
#2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
a=int(input('sayi giriniz:'))
if a<0:
    if(a%2==0):
         print('sayi negatif ve çifttir')
    print('sayi negatif tektir')
elif a>0:
    if(a%2==0):
         print('sayi pozitif ve çifttir')
    print('sayi pozitif tektir')
else:
    print('sayi sifirdir')
#3- email ve parola bilgileri ile giriş kontrolü yapınız
email='seyma@gmail.com'
parola='123'
a=str(input('mail giriniz:'))
b=int(input('parola giriniz:'))
if a==email:
    if b==parola:
        print('giriş yapildi')
    else:
        print('parola yanlis')
else:
    print('mail yanlis')

#4- girilen 3 sayıyının en büyüğünü bulun
a=int(input('birinci sayiyi giriniz:'))
b=int(input('ikinci sayiyi giriniz:'))
c=int(input('ücüncü sayiyi giriniz:'))

if(a>b and a>c):
    print('a en büyük sayidir')
elif(b>a and b>c):
    print('a en büyük sayidir')
if(c>a and c>b):
    print('a en büyük sayidir')
"""
#5-kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayınız 
#  eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın 
#  a-ortalama 50 olsa bile final notu en az 50 olmalıdır 
#  b-finalden 70 alındığında ortalamanın önemi kalmasın
"""
vize1=float(input('vize1 notu:'))
vize2=float(input('vize2 notu:'))
final=float(input('final notu:'))
ort= ((((vize1+vize2)/2)*60)/100)+(final*40/100)
if ort>=50:
    if 50<=final<70:
        print('geçtiniz')
    else:
       print('geçmek icin final notu en az 50 olmalidir')
elif final>=70:
    print('geçtiniz')
else:
    print('kaldiniz')
"""
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
if 0<indeks<18.5:
    print('zayifsiniz')
elif 18.5<=indeks<25:
    print('normalsiniz') 
elif 25<=indeks<30:
    print('normalsiniz') 
else:
    print('obezsiniz')
