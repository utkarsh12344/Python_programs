'''Introduction Of Class'''

class Student:#class name; Generally, first letter becomes capital letter
    
    country="Turkey" # class attribute
    
    def __init__(self, name,surname,age,school):# instance attribute
        self.name = name
        self.surname=surname
        self.age = age
        self.school=school
        
# instantiate the Student class        
st1=Student("Arif","Mandal",21,"AGU")
st2=Student("Ceyhun","Buyuk",20,"ODTU")

print(st1.country)

print("St1 name {} , surname {} , age {} , school {}".format(st1.name,st1.surname,st1.age,st1.school))#show the screen

print("St2 name {} , surname {} , age {} , school {}".format(st2.name,st2.surname,st2.age,st2.school))#show the screen







        
    
        
Turkey
St1 name Arif , surname Mandal , age 21 , school AGU
St2 name Ceyhun , surname Buyuk , age 20 , school ODTU
'''Methods in Class'''
class Student:#class name; Generally, first letter becomes capital letter
    
    country="Turkey" # class attribute
    
    def __init__(self, name,surname,age,school):# instance attribute
        self.name = name
        self.surname=surname
        self.age = age
        self.school=school
    
    #Setter and Getter
    #NAME
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    
    #SURNAME
    def setSurname(self,surname):
        self.surname=surname
    def getSurname(self):
        return self.surname
    
    #AGE
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
    
    #SCHOOL
    def setSchool(self,school):
        self.school=school
    def getSchool(self):
        return self.school
    
    #Other Method
    
    #SHOW information
    
    def showInfo(self):
        print("All Information:")
        print('''                 Name= {}
                 Surname={}
                 Age={}
                 School={}
                 '''.format(self.name,self.surname,self.age,self.school))
                
        
# instantiate the Student class        
st1=Student("Arif","Mandal",21,"AGU")
st2=Student("Ceyhun","Buyuk",20,"ODTU")

print("St1 name {} , surname {} , age {} , school {}".format(st1.name,st1.surname,st1.age,st1.school))

st1.setName("Kerim")

print("St1 name {} , surname {} , age {} , school {}".format(st1.name,st1.surname,st1.age,st1.school))

n=st1.getName()
print(n)

print("Student1")
st1.showInfo()

print("Student2")
st2.showInfo()
St1 name Arif , surname Mandal , age 21 , school AGU
St1 name Kerim , surname Mandal , age 21 , school AGU
Kerim
Student1
All Information:
                 Name= Kerim
                 Surname=Mandal
                 Age=21
                 School=AGU
                 
Student2
All Information:
                 Name= Ceyhun
                 Surname=Buyuk
                 Age=20
                 School=ODTU
                 
'''Example of Class(Circle)'''

class Circle:
    pi=3.14
    
    # instance attribute
    def __init__(self,radius=2):#radius=2 default value; if user not defined radius, radius it will be 2
        self.radius=radius
    
    #setter and getter
    
    def setRadius(self,radius):
        self.radius=radius
    
    def getRadius(self):
        return self.radius
    
    #AREA METHODS
    def area(self):
        return (self.radius**2)*Circle.pi
    
    #CIRCUMFERENCE METHODS
    def cir(self):
        return 2*Circle.pi*self.radius
    


#create object

c1=Circle()

print("Default radius of circle 1 is ", c1.getRadius())#default value of Circle

c1.setRadius(4)

area=c1.area()

print("Area of circle 1=",area)

circumference=c1.cir()

print("Circumference of circle 1=",circumference)

#create other object
c2=Circle(10)

print("c2 radius=",c2.getRadius())

print("Area of circle 2=",c2.area())

print("Circumference of circle 2=",c2.cir())

        
    
Default radius of circle 1 is  2
Area of circle 1= 50.24
Circumference of circle 1= 25.12
c2 radius= 10
Area of circle 2= 314.0
Circumference of circle 2= 62.800000000000004
'''Example of Class(Point)'''

class Point:
    
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    
    #GETTER AND SETTER
    
    def setx1(self,x1):
        self.x1=x1
    
    def getx1(self):
        return x1

    def sety1(self,y1):
        self.y1=y1
    
    def gety1(self):
        return y1
    
    def setx2(self,x2):
        self.x2=x2
    
    def getx2(self):
        return x2

    def sety2(self,y2):
        self.y2=y2
    
    def gety2(self):
        return y2
    
    #distance
    
    def distance(self):
        return ((self.x1-self.x2)**2 +(self.y1-self.y2)**2)**0.5
    
    #slope
    
    def slope(self):
        return int((self.y1-self.y2)/(self.x1-self.x2))
    

p1=Point(1,2,3,4)

print("A(",p1.x1,",",p1.y1,")","B(",p1.x2,",",p1.y2,")")

print("Distance two point=",p1.distance())

print("Slope of two point=",p1.slope())

p1.setx1(5)
p1.sety2(8)

print("New slope of two point=",p1.slope())
    
A( 1 , 2 ) B( 3 , 4 )
Distance two point= 2.8284271247461903
Slope of two point= 1
New slope of two point= -3



'''Inheritance'''

# parent class
class Animal:
    
    def __init__(self):
        print("Animal created")
        
    def who(self):
        print("Animal")
        
    def eat(self):
        print("Eating...")
    
    def sleep(self):
        print("Sleeping...")
        

# child class

class Bird(Animal):
    
    def __init__(self):
        # call super() function
        print("Bird created")
        super().__init__()
        
    def who(self):
        print("Bird")     
        
    def fly(self):
        print("Fyling...")
        

flappy=Bird()

print(flappy.who())

print(flappy.eat())

print(flappy.sleep())

print(flappy.fly())


        


