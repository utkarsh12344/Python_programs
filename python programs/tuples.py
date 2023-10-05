tuple1=("utkasrh","bondade",1,2,3,4)
print(tuple1)
print(len(tuple1))
print(tuple1[3])

for x in dir(tuple):
    if"_" not in x:
        print(x)
