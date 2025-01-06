#NESNE TABANLI PROGRAMLAMA
"""
#class
class Person: #claslar attribute ve method içerirler
    #class attibute
    adress='no information'#direk clasın içinde tanımlanır ve kullanılır

    #constructor (yapıcı metod)
    def __init__(self,name,year):#bu fonksiyon yapısı bir obje kullanarak clasta işlemler yapacaktır
        self.name=name            #eğer bu fonksiyonu objeyle çağırıyorsam name ve year parametrelerini göndermek zorundayım
        self.year=year

    #instance methods
    def intro(self):#class içerisinde bir ilemi yüklenen method tanımladık
        print('hello'+ self.name)#self objeyi temsil eder ve hangi objeden çağırılırsa onlar kullanılır
    def calculateAge(self):#değer döndüren bir method da oluşturulabilir
        return 2024-self.year


#object(instance)
p1=Person(name='ali',year=1990) #clası(klastaki fonksiyonu kullanabilmek için paremetrelerle beraber) kullanarak bir obje tanımladık 
p2=Person('ada',2000) 
#updateing
p1.name='ahmet' #bu şekilde objedeki bilgiyi değiştirebilirim
p1.intro()#clastaki bir methodu çalıştırdık
print(f'yaşim:{p2.calculateAge()}')
print(f'name:{p1.name} year:{p1.year} adres:{p1.adress}')

class Circle:
    pi=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle()#parametre girmediğimiz için varsayılan değere göre class çalışır
c2=Circle(5)#5 değeri için class kullanılır
print(f'c1:alan:{c1.alan_hesapla} cevre={c1.cevre_hesapla}')
print(f'c2:alan:{c2.alan_hesapla} cevre={c2.cevre_hesapla}')

#INHERITANCE(KALITIM)#temel bir sınıfın özellikleri özel başka sınıflarda kullanılabilir
class Person(): #sınıfın oluşturulduğunu bildiren bir sınıf oluşturduk
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('Person created')
    
    def who_am_i(self):
        print('i am a person')

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)#miras alacağımız sınıfı sınıfımızın içerisinde tanımlamamız gerekir
        self.studentNumber=number
        print('Student created')
    #override #bu işlem temel sınıftaki aynı isimli fonksiyonu ezer
    def who_am_i(self):
        print('i am a student')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch=branch
    def who_am_i(self): #başka bir classtaki özelliklere kendi bilgilerini ekleyerek kullanıyor
        print(f'i am a {self.branch} teacher')


p1=Person('ali','yilmaz')#parametrelerimizi yollayarak objelerimizi oluşturduk
s1=Student('seyma','tuba',1234)
t1=Teacher('ada','yilmaz','math')
t1.who_am_i()

print(p1.firstName+' '+p1.lastName)
print(s1.firstName +' '+ s1.lastName+' '+ str(s1.studentNumber))
p1.who_am_i() #person sınıfındaki fonk çalışır
s1.who_am_i() #student sınıfında olmamasına rağmen bağlı olduğu person sınıfındaki fonk çalışırdı fakat student içinde de aynı fonk tanımlandığı için artık o çalışır

#SPECİAL METHODS
class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('movie objesi oluşturuldu')
    def __str__(self): #sınıfımızın içerisinde işlemler yapan fonksiyonlar oluşturduk
        return f"{self.title} by {self.director}"
    def __len__(self): #len liste şeklindeki ifadeler için kolayca kullanılan bir method iken sınıflar içerisinde tanımlanması gerekir
        return self.duration
    def __del__(self):
        print('movie silindi')


m=Movie('film adi','yönetmen adi',120)#del methodu kullanılmasa bile obje br zaman sonra kendi silinir ve mesaj yazar 
del m #oluşturduğumuz objeyi böyle silebiliriz ve sınıfımızdaki del fonksiyonu gereği mesaj yazar
print(len(m)) # obje silindiği için hata verir 
print(str(m)) #str fonk çalışır eğer silinmeseydi 
"""
#QUİZ UYGULAMASI
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions= questions
        self.score=0
        self.guestionİndex=0
    def getQuestion(self):
        return self.questions[self.guestionİndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'soru {self.guestionİndex +1}:{question.text}')

        for q in question.choices:
            print('-'+q)
        
        answer=input('cevap:')
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.guestionİndex +=1

    def loadQuestion(self):
        if len(self.questions)==self.guestionİndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.guestionİndex+1

        if questionNumber>totalQuestion:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100),'*')


    def showScore(self):
        print('score:',self.score)




q1=Question('en iyi propramlama dili hangisidir?',['c#','python','java','javascript','html'],'python')
q2=Question('en popüler propramlama dili hangisidir?',['c#','python','java','javascript','html'],'python')
q3=Question('en çok kazandiran propramlama dili hangisidir?',['c#','python','java','javascript','html'],'python')
questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.loadQuestion()

#print(q1.checkAnswer('python'))

        