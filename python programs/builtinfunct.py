'''abs()'''

x=-20

print(abs(x))#abs stand for absolute so returns positive value of variable

'''round()'''

print(round(22/7))#exact result must be 3.14 round function roll closest number.Also,
#the function take 2 parameter first parameter original number, second parameter how many digit that you want

print(round(22/7, 3))

'''all()'''

l=[1,2,4,7,8,]

print(all(l))#returns true if all values in a list are True.If any of these values is False, then False is to return the value. 

l2=[0,2,4,6]

print(all(l2))

'''any()'''

l3=["Arif","Mandal",""]

print(any(l3))#The task of any () function If at least one of all values in an array is True, True is output.

'''bin()'''

print(bin(12))#returns binary format

'''ord()'''

print(ord("a"))#Returns the decimal number that a character corresponds to.

print(ord("q"))

'''oct()'''

print(oct(24))#returns a number to its equivalent in octal order

'''hex()'''

print(hex(32))#returns a number to its equivalent in hexadecimal order

'''copyright()'''

print(copyright())#You may access Python's copyright information.

'''dir()'''

print(dir())#If we use dir () without parameters, we get a list of items in the current namespace

'''divmod()'''

print(divmod(10,5))#The first parameter returns the partition portion of the partition operation and the second element returns the remainder.

'''enumerate()'''

print(list(enumerate('Python')))#returns numbered list.

for i in enumerate('Python'):#the other way
     print(i)

'''exit()'''

#exit()  #This function allows you to exit the currently running program.

'''help()'''

print(help(dir))#Using this function, we can access the help documentation for items in the Python programming language.

'''filter()'''

print([i for i in l if i % 2 == 1 ])#this is classic way of find odd numbers

def odd(number):
    return number%2==1

print (*filter(odd, l))#With this built-in function, we can apply a filtering based on a specific criterion on the elements in array objects.

'''len()'''

string="Python"

l=["python","java","php","javascript","c"]

print(len(string))#returns length of string, list, set etc.

print(len(l))

'''map()'''

l=[1,2,3,4,5,6,7,8,9]

def square(l):
    return l**2

print(list(map(square,l)))#takes 2 parameter first parameter is intended function, other parameter is list

'''max()'''

tuples=(1,4,7,25,69,12)

print(max(tuples))#returns maximum value in tuples, list etc.

languages =[ 'python' , 'ruby' , 'go' , 'r' , 'java' , 'assembly' ]

print(max(languages, key=len ))#string version

'''mix()'''

tuples=(1,4,7,25,69,12)

print(min(tuples))#it is similar with max it returns minimum value in tuples, list etc

languages =[ 'python' , 'ruby' , 'go' , 'r' , 'java' , 'assembly' ]

print(min(languages, key=len ))#string version

'''pow'''

print(pow(3,2))#returns 3^2=9

print(pow(3,2,3))#The third parameter allows us to calculate the modulus of the number obtained by the force calculation.

'''quit()'''

#quit() #we use to exit the kernel

'''range()'''

for i in range(0,10,2):#we use to list numbers in a certain range.
    print(i)
    

'''reversed()'''

languages =[ 'python' , 'ruby' , 'go' , 'r' , 'java' , 'assembly' ]

print(list(reversed(languages)))#returns inverse list

print(languages[::-1])#classic way that learned before

'''sorted()'''

languages =[ 'python' , 'ruby' , 'go' , 'r' , 'java' , 'assembly' ]

numList=[4,45,12,5,89,24]

print(list(sorted(languages)))#returns sorted list.

print(list(sorted(numList)))#for numbers

'''sum()'''

numList=[4,45,12,5,89,24]

print(sum(numList))#returns summation of numList

'''type()'''

print(type("Turkey"))#it is to say what type of data an object belongs to.

'''zip()'''

a1=["a","b","c","d","e"]

a2=[1,2,3,4,5]

print(list(zip(a1,a2)))#returns matching items by order

print(*zip(a1,a2))#second way

for i,j in zip(a1,a2):#third way
    print(i,j)

    
'''vars()'''

print(vars(str))#returns methods and properties of objects

'''
End of Built-in Function 
Thank you
'''
