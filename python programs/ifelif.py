num1=200
num2=200

if num1<num2:
    print("num2 is greater than num1")

if num1<num2:
    print("num2 greater than num1")
elif num1>num2:
    print("num1 greater than num2")
elif num1==num2:
    print("both are equal")


b1=False
b2=True

#and
if b1 and b2:#checks two variable value if someone is false returns false
    print("False")
else:
    print("True")
    

#or
if b1 or b2:##checks two variable value if someone is true returns true
    print("False")
else:
    print("True")

#These are usual logical conditions:
#1)Equals: a == b
#2)Not Equals: a != b
#3)Less than: a < b
#4)Less than or equal to: a <= b
#5)Greater than: a > b
#6)Greater than or equal to: a >= b

num1=20
num2=30

#version1
if num2>num1: #if statement to test whether num2 is greater than num1. if num2 greater than num1; print the screen else nothing
    print("Number2 greater than number1")



#version2
if num2>num1:
    print("Number2 greater than number1")
elif num2<num1:#if the previous conditions were not true, then try this condition
    print("Number1 greater than number2")
elif num2==num1:
    print("Number1 equals number2")
    


#version3
if num2>num1:
    print("Number2 greater than number1")
elif num2<num1:
    print("Number1 greater than number2")
elif num2==num1:
    print("Number1 equals number2")
else:#catches anything which isn't caught by the preceding conditions.
    print("Some error but I dont know...")



#Short hand
print("num1") if num1 > num2 else print("=") if num1 == num2 else print("num2")


b1=False
b2=True

#and
if b1 and b2:#checks two variable value if someone is false returns false
    print("False")
else:
    print("True")
    

#or
if b1 or b2:##checks two variable value if someone is true returns true
    print("False")
else:
    print("True")

    
#EXAMPLE:
#1)odd or even:

a=int(input("enter the number :"))
if a%2==0:
    print("even")
else:
    print("odd")

b=int(input("enter ur age :"))
if b>=18:
    print("you are adult")
elif b<=18 and b>=10:
    print("you are teenager")
else:
    print("you are child")

