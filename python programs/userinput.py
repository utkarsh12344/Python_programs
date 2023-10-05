#user input-------
user_input=input("What is your name: ")
print("Welcome ",user_input)

#input fuction accept only string variable

number=input("Enter the any number: ")
number2=5
#print(number+number2)

#gave a this error; TypeError: must be str, not int 
#thus first must convert int


number=int(input("Enter the any number: "))
number2=5
print(number+number2)#now there is not any problem


#the other solution
number=int(input("Enter the any number: "))
number2=5
print(int(number)+number2)#now there is not any problem