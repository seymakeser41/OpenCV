#PYTHONDA LİSTELER 
"""
my_list=[1,2,3] #liste oluşturma
my_list=["bir",2,True,5.6]  #liste içinde farklı türde eleman olabilir

list1=["one","two","there"]
list2=["four","five","six"]
numbers= list1 + list2 #listeler + operatörü ile toplanır , birleşir
print(len(numbers)) #listelerin uzunluğu, eleman sayısı len fonksiyonu ile bulunur
print(numbers[2]) #listelerin elemanlarına indeks sayıları cağırılarak ulaşılır

userA=["Şeyma",19]
userB=["Ali",30]
users= [userA , userB] #liste içerinde listeleri oluşturur 
a=users[1]
print(a[0]) #liste içerisindeki 1. indeksi listenin 0. indeksli elemanını verir
print(users[1][0]) #aynı işlem bu şekildede olabilir
"""
"""
#PYTHON LİSTELER ÖRNEKLER
#1-"Bmw, Mercedes, Opel, Mazda " elemanlarına sahip bir liste oluşturun.
cars=["Bmw", "Mercedes", "Opel", "Mazda"]
#2- Liste kaç elemanlıdır
print(len(cars))
#3-listenin ilk ve son elemanı nedir
ilk=cars[0]
son=cars[-1]
#4-Mazda değerini Toyota ile değiştirin
cars[3]="Toyota"
print(cars)
#5-Mercedes listenin bir elemanı mıdır
result="Mercedes" in cars
#6-listenin -2 indeksindeki değeri nedir
print(cars[-2])
#7-listenin ilk üç elemanını alın
print(cars[0:3])
#8-listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekle
result=cars[-2:]=["Toyota","Renault"]
#9- listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
result=cars+ ["Audi","Nissan"]
#10- listenin son elemanını silin
del cars[-1]
result=cars
#11- liste elemanlaını tersten yazdırın
result=cars[::-1]
print(result)
#12- aşağıdaki verileri bir liste içerisinde saklayınız 
  #studentA: Yiğit Bilgi 2010, (70,60,70)
  #studentB: Sena Turan 1999, (80,80,70)
  #studentC: Ahmet Turan 1998, (80,70,90)

studentA= ['Yiğit','Bilgi',2010,[70,60,70]]
studentB= ['Sena','Turan',1999,[80,80,70]]
studentC= ['Ahmet','Turan',1998,[80,70,90]]
#13-liste elemanlarını ekrana yazdırın
result=studentA[3][0]
"""
#PYTHON LİSTE METHODLARI
"""
numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
val =min(numbers) #sayıların minimum olanını verir
val =max(numbers) #sayıların maksimum olanını verir
val =min(letters) #string ifadelerin alfabetik olarak minimum olanını verir
val =max(letters) #string ifadelerin alfabetik olarak maksimum olanını verir

val=numbers[3:6]  #3. indeksten 6 ya kadarını alır
numbers[4] =40 #listelerin elemanları değiştirilebilir
numbers.append('49')#listeye sondan ekler 
numbers.insert(3,45) #listenin 3. indeksine 45 sayısını ekler 
numbers.pop() #sondaki elemanı siler;eğer indeks belirtilirse onu siler
numbers.remove(16)# belirttiğiniz elemanı siler
numbers.sort() #küçükten büyüğe sayısal olarak sıralanır
letters.sort()#küçükten büyüğe alfabetik olarak sıralanır
numbers.reverse() #tersten yazar 
numbers.count(20) #20 elemanı numbers listesinde kaç tane var öğreniriz
numbers.clear() #listeyi temizler, boşaltır
"""
#PYTHON LİSTE METHODLARI ÖRNEKLER
names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]
#1-"cenk"ismini listenin sonuna ekleyiniz
names.append('Cenk')
#2-"Sena" ismini listenin başına ekleyiniz 
names.insert(0,'Sena')
#3- 'Deniz ismini listeden siliniz
names.pop()
names.remove('Deniz')
#4- 'Deniz' isminin indeksi nedir
index =names.index('Deniz')
#5- 'Ali' listenin bir elemanı mıdır
result = 'Ali' in names
#6- liste elemanlarını ters çevirin 
result= names.reverse()
#7- liste elemanlarını alfabetik olarak sıralayınız
result= names.sort()
#8- years listesini rakamsal büyüğe göre sıralayınız
result= years.sort()
#9- str="Chevrolet,Dacia" karakter dizisini listeye çeviriniz
str= "Chevrolet, Dacia"
result = str.split(',')
#10- years dizisinin en büyük ve en küçük elemanı nedir
min= min(years)
max= max(years)
#11- years dizisinde kaç tane 1998 değeri vardır 
years.count(1998)
#12- years dizinde tüm elemanlarını siliniz 
years.clear()
#13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar= []
marka=input("marka: ")
markalar.append(marka)
marka1=input("marka: ")
markalar.append(marka1)
marka2=input("marka: ")
markalar.append(marka2)

#PYTHON TUPLE
tuple= (1,'iki',3)
tuple[0]='Deniz' #bu yanlistır, hata verir, tuple'ın elemanları tek tek değiştirilemez
names=('esra','emel','ayşe')
result= names + tuple #iki tuple böyle toplanır, birleşir
