print("hello world")
print("i am fine")
if 18>9:
    print("18 is greater then 9")
    print("18 is greater then 8")
#to avoid indentation error use atleast one /four spaces 
#and lines should be in same line 

x=50
z="itachi uchiha"
print(x)
print(z)
print(type(x))
print(type(z))

#multi variable declaration

x,y,z="cricket","football","relay"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x="shit"
def myfunc():
    print("python is "+x)
myfunc()

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
x = ("apple", "banana", "cherry")
print(x)
print(type(x))

x=range(8)
print(x)
print(type(x))

x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(x)
print(type(x))

x1="hello world"
print(x)
print(type(x))
#looping through astring
for x in 'bollywood':
    print(x)

#string length
a="thikhu"
print(len(a))

#chack string
b="you are good at maths"
print("maths" in b)

txt="you are very special"
if "in" in txt:
    print("yes,'in' is present")
d="i am fine"
print(d.upper())
print(d.lower())
print(d.strip())
print(d.replace("i","you"))

car="mercedes"
house="bunglow"
pet="dog"

f="i am utkarsh i will have car named {} and house type  {} and also have a {}"
print(f.format(car,house,pet ))
print(f.capitalize())
print(f.casefold())
#print(f.center())
f1="i am goodii"
print(f1.count(i))


