#PYTHON OPERATÖRLERİ_4.KLASÖR
#ATAMA OPERATÖRLERİ
x =5
x = x+5 #eşittir ile sağdaki ifade sola atanır
x+=5 #yukarıdaki ifadenin kısa gösterimidir
x-=5 #x=x-5 demektir
x*=5 #x=x*5 demektir
x/=5 #x=x/5 demektir
x%=5 #x=x%5 demektir (kalanı verir)
x//=5 #x=x//5 demektir (tam kısmı alır)
x**=5 #x=x**5 demektir (üssünü alır)

values= 1,2,3 #tuple liste tipinde oluşturduk 
a,b,c = values # listedeki değerleri sırasıyla atar , eğer listede yeteri kadar değer yoksa hata verir , fazla değerde de hata verir
values_1=1,2,3,4,5
e,d,*f=values_1 #yıldız ıle fazla değerler o elemana dizi olarak atanır 
#3print(e,d,f) #1 2 [3,4,5]

#ATAMA OPERATÖRLERİ UYGULAMA 
x,y,z= 2,5,107
numbers= 1,5,7,10,6
#1-Kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı nedir
sayi_1=int(input("birinci sayiyi giriniz:"))
sayi_2=int(input("ikinci sayiyi giriniz:"))
result= (sayi_1*sayi_2)-(x+y+z)
print(result)

#2-y'nin x'e kalansız bölümünü hesaplayınız 
result=y//x
print(result)

#3-(x,y,z) toplamının mod 3'ü nedir
result = (x+y+z)%3

#4- y'nin x. kuvvetini hesapla
result=y**x

#5- x,*y,z= numbers işlemine göre z'nin küpü kaçtır?
x,*y,z= numbers
result=z**3

#6-x,*y,z= numbers işlemine göre y nin değerleri toplamı kaçtır ?
x,*y,z= numbers
result= y[0]+y[1]+y[2]
