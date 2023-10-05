string="Arif Mandal" #Index of string start 0,1,2,3...
print(string[1])#it gives indexing character

print(string[0:3])# start from 0(0 include) but 3 not include

print(string[:])#all string

print(string[::-1])#reverse of string

print(len(string))#it gives length of string

print(string.lower())#returns the string in lower case

print(string.upper())#returns the string in upper case

print(string.split(","))#returns ["Arif","mandal"]

print(string.replace("A","D"))#replaces a string with another string

print(string.isdigit())#it checks digit or not so return false

print(string.isalpha())#it checks alpha or not so return false

print(string.isprintable())#it checks printable or not so return true

print(string.index("a"))#returns index of a