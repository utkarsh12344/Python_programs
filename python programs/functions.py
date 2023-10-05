#calling a function a no of times

def write_name():
    print("utkarsh bondade")
    print("python")

write_name()
write_name()
write_name()

#adding two numbers--------
def summation(num1,num2):
    print(num1+num2)

summation(40,60)
summation(100,140)


#default parameter-----
def country(country="turkey"):
    print("my country ",country)
country()
country("usa")



#we use return in function------
def evenOdd(num):
    if num%2==0:
       return "even"
    else:
        return "odd"
 
evenOdd(15)


#flexible parameters-----
def mult(*args):
    result=1
    for i in args:
        result*=1
    return result
print(mult(1,1,2,3,5,8,13,21,34))


#Fibonacci-------
def fib(num):
    if num==1:
        return [1]
    elif num==2:
        return [1,1]
    else:
        lst=fib(num-1)
        return lst +[lst[-1]+lst[-2]]
fib(10)


