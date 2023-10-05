#Error handling (exception handling) is a way to ensure 
#that your program responds to the error in our own way rather than giving an error message 
#and stopping work in unexpected situations. Error detection is an important part of Python programming,
# allowing your program to run reliably without making it too complicated.

#General format of try except
try:
    print(x)
except:
    print("Error...") #because x not defined
    
print("******************************************************************")
#Actually this error type NameError. Let's try this.

try:
    print(y)
except NameError:
    print("Value error your programming includes not defined variable.")
    
print("******************************************************************")

#We can define as many exception blocks as you want
try:
    print(var)
except NameError:
    print("Name Error.")
    
except:
    print("Something is wrong. ")
    
print("******************************************************************")
#finally block:
#it will be executed regardless if the try block raises an error or not.

try:
    x=15/0
    print(x)
except ZeroDivisionError:
    print("Zero division error.")
    
finally:
    print("Codes continues in here...")

print("******************************************************************")


#Using Raise:
raise NameError('HiThere')
    
    
print("******************************************************************")
#Some Error Example
#1)Index error:
try:
    list1=["python","java",1889,1994]
    print(list1[4])
except IndexError:
    print("INDEX ERROR...")

    
print("******************************************************************")


#2)IOError:

try: 
    fileName="file.txt"
    f=open(fileName,"r")
except IOError:
    print("IOError... File not exits")
    
print("******************************************************************")
#3)ValueError:

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("That was no valid number.Try again...")
 
