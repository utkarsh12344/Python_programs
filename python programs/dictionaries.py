dict1={"rohit":"batsman","virat":"batsman","raina":"left batsman","dhoni":"rightbatsman"}
print(dict1)
print(dict1["dhoni"])

for i in dict1:
    print(i)
for i,j in dict1.items():
    print(i,"---",j)
dict1["virat"]="best batsman"
for i,j in dict1.items():
    print(i,"---",j)

del dict1["virat"]
print(dict1)

dict1.clear()
print(dict1)

for x in dir(dict1):
    if "_" not in x:
        print(x)