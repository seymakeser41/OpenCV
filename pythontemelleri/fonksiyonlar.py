#FONKSİYONLAR
"""
def sayHello():
    print('hello')
sayHello() #fonksiyon oluşturduk ve çağırdığımızda fonk bünyesindeki işlem gerçekleşti
def sayHello(name='user'):# fonksiyonlar parametre alarak o parametreyi kullanarak işlem yapabilir
    print('hello '+ name) #parametre gönderilmezse belirttiğimiz varsayılan değer kullanılır
sayHello('seyma')
def sayHello(name='user'):# fonksiyonlar değer döndürerek sonucun kullanılmasını sağlayabilir
    return ('hello '+ name) 
msg=sayHello('seyma')
print(msg)

def total(num1,num2):#parametre alıp değer döndüreren toplama işlemi yapan bir fonksiyon
    return num1+num2
result=total(30,40)
print(result)

def yas(dg):
    return 2024-dg
ageseyma=yas(2005)
print(ageseyma)

def emeklilik(dg, isim):# doğum yıllına göre emekliliğe ne kadar kaldığını gösteren fonksiyon
    yas=yas(dg)
    emekli=65-yas
    if emekli>0:
        print(f'emekliliğe {emekli} yil kaldi')
    else:
        print(f'zaten emeklisinzi')

#PARAMETRELER
def change(n):
    n[0]='istanbul'
sehirler=['ankara','izmir']
n=sehirler[:] #bir kopyalama işlemi gerçekleştirildi
n[0]='istanbul' 
print(sehirler)
print(n)

def add (a,b,c=0):#fonk 2 veya 3 eleman alabilecek hale geldi
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))
def add (*params):#ilk örnek çok sayıda işlemde sıkıntılı iken böyle yaparak istediğimiz kadar değer girebiliriz
    return sum((params))#tek yıldız bir tuple oluşturur
print(add(10,20))
print(add(10,20,30))

def displayUser(**args):#2 yıldız dictionary olduğunu bildirir
    for key,value in args.items():
        print('{}is {}'.format(key,value))
displayUser(name='cinar', age=2, city='ankara')
displayUser(name='seyma', age=12, city='istanbul',phone='67890')
displayUser(name='cinar', age=2, city='ankara',phone='3456789',email='refrkmkmf')

def myFunc(a,b,c,*args,**kwargs):# parametre değerlerimize uygun girdiğimiz değerleri kendi gruplar
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50,60,70,key1='value1',key2='value2')

#UYGULAMALAR
#1-gönderilen bir kelimeyi belirtilen kez ekranda ekranda gösteren fonksiyonu yazın.
def name(name,a):
    print(name  *a)
a=int(input('kelimeyi kaç kez yazmak istiyorsunuz:'))
name1=str(input('kelimeyi girin:'))
name(name1 ,a)

#2-kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
def listcevir(*params):
    list=[]
    for param in params:
        list.append(param)
    return list
result=listcevir(1,4,7,34,26,98)
print(result)
"""
"""
#3-gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz
def asalbul(a,b):
    i=2
    while a<=b:
       while i<=int(a/2):
           if a%i==0:
             i+=1
             break
           else:
              print(a)
              break    
       a+=1
a=int(input('araliktaki kücük sayiyi girin'))
b=int(input('araliktaki büyük sayiyi girin'))
asalbul(a,b)
"""
"""
#4-Kendisine gönderilen sayıların tam bölenlerini bir liste oluşturan fonk
def bölen(a):
   list=[]
   i=1
   while i<=a:
      if a%i==0:
         list.append(i)
      i+=1
   return list
a=int(input('bölenlerini bulmak istediğiniz sayiyi girin'))
print(bölen(a))

#lambda
def square(num):return num**2
numbers=[1,3,5,9]
result=list(map(square,numbers)) #map ile alınan değerler listeye çevirilir
for item in map(square,numbers): # listeye çevirilen bu değer yazdırıldı
    print(item)

result=list(map(lambda num:num**2, numbers)) #aynı işlem bu şekilde lambda kullanılarak da yapılabilir
print(result)

#filter
check_even=lambda num: num%2==0 #çiftleri alır ve tekler filtreden geçmez 
result=list(filter(check_even,numbers))
print(result)

#global ve yerel değişkenler 
x='global x'
def fonk():
    x='local x'
    print(x) # fonksiyon içnde çaliştiği için local değeri verir
fonk()
print(x)# fonksiyon dışında tanımlanmış değer için geçerlidir ve global değeri verir

name='seyma' # önce fonk çalışıp ada yazar sonra global değişken yazılır
def changename(new_name):
    name=new_name
    print(name)
changename('ada')
print(name)

name='global string' #fonksiyon içindekiler tanımlanan bir önceki değeri baz alır name çınar olur
def greeting():
    name='cinar'
    def hello():
        print('hello'+name)
    hello()
greeting()

x=50 #dışarıda x 50 olur fonka 50 geçer içerde 100 olur ve 100 yazar
def test(x):
    print('x'+ x)
    x=100
    print(f'c changed x to{x}')
test(x)
"""
#BANKAMATİK UYGULAMASI 
sadikhesap={
    'ad':'sadik turan',
    'hesapno':'1234567',
    'bakiye':3000,
    'ekhesap':2000
}
alihesap={
    'ad':'ali turan',
    'hesapno':'1234568',
    'bakiye':2000,
    'ekhesap':1000
}
def paracek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranizi alabilirsiniz')
        bakiyesorgula(sadikhesap)
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']
        if toplam>=miktar:
            ekhesap_kullanimi=input('ek hesap kullanilsin mi(e/h)')
            if ekhesap_kullanimi=='e':
                bakiye=hesap['bakiye']
                ekhesap_kullanimi_miktar=miktar-bakiye
                hesap['bakiye']=0
                hesap['ekhesap']-=ekhesap_kullanimi_miktar
                print('paranizi alabilirsiniz')
                bakiyesorgula(sadikhesap)
            else:
                print(f'{hesap['hesapno']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir')
        else:
            print('paraniz yetersiz')
def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadir.ek hesap limitiniz ise{hesap['ekhesap']}tl bulunmaktadir")

paracek(sadikhesap,3000)
print('********************')
paracek(sadikhesap,1000)
