#PYTHON DİCTİONARY
"""
plakalar={'Kocaeli':41 , 'İstanbul':34} #key ve value olucak şekilde ikili biçimde tanımlanır
print(plakalar['Kocaeli'])# kocaelinin değerini yazdırır
plakalar['ankara']= 6 # ankara bir key olarak ve değeri 6 olarak eklendi
plakalar['Kocaeli']='new value' #kocaeli keyine yeni değeri atar 

users ={
    'sadikturan': 36,
    'cinarturan':2
}
print(users['cinanturan'])

users={
    'sadikturan':{
       'age':36,
       'roles':['user'],
       'email': 'sadik@gmail.com',
       'address': 'kocaeli',
       'phone':'1231321'
    },
    'cinarturan':{
        'age':2,
        'roles':['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone':'1231321'
    }
}
print(users['cinarturan']['roles'][0])# dictionary içinde dictionary oluşturduk
"""
#PYTHON DİCTİONARY ÖRNEKLER
'''
ogrenciler={
    '120':{
        'ad':'ali',
        'soyad':'yılmaz',
        'telefon':'532 000 0000'
    },
    '125':{
        'ad':'can',
        'soyad':'korkmaz',
        'telefon':'532 000 0001'
    },
    '128':{
        'ad':'volkan',
        'soyad':'yükselen',
        'telefon':'532 000 0002'
    }
}
'''
'''
#1- bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
ogrenciler={}
number=input("öğrenci no:")
name=input("öğrenci ad:")
surname=input("öğrenci soyad:")
phone=input("öğrenci telno:")

ogrenciler[number]={
    'ad':name,
    'soyad':surname,
    'telefon':phone 
}

ogrenciler.update({ #bununla dictionarye birden fazla ekleme yapabiliriz
    number:{
        'ad':name,
    'soyad':surname,
    'telefon':phone 

    }
})

#2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
print(ogrenciler)

ogrno=input('çğrenci no:')
ogrenci=ogrenciler[ogrno]
print(ogrenci)
'''
#PYTHON SETS
'''
fruits={'orange','apple','banana'} #setin elemanlarına indeks kullanarak(fruits[0]) şeklinde ulaşamayız
for x in fruits: #setlerin elemanlarına döngü ile ulaşabiliriz
    print(x)
fruits.add('cherry')#bununla setin içine eleman eklenir
fruits.update(['mango','grape']) #eğer birden çok şey  eklemek istersek bu method kullanılır
mylist=[1,2,5,4,4,2,1,]
print(set(mylist)) #setlerde tekrarlayan eleman olmaz , bir tane alır
fruits.remove('mango') #setden belirtilen ögeyi siler
fruits.discard('apple') #setden belirtilen ögeyi siler
fruits.pop() #sondan siler ama setler sıralı olmadığından neyi sileceği belli olmaz
fruits.clear() #set temizlenir
'''
#PYTHON REFERANCE
a=['apple','banana']
b=['apple','banana']
a=b #iki liste eşitlenerek aynı adresi taşımış oldu ve birinde yapılan değişiklik diğerini de etkilicek
b[0]='grape'

