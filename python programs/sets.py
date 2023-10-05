set1={"python","java","c","c++"}
print(set1)

for i in set1:
    print(i)
print(len(set1))
set1.add("php")
print(set1)
set1.remove("c")
print(set1)
set1.pop()
print(set1)
#set1.clear()
print(set1)
set2={"mongodb","react","node","c++"}
print(set2.intersection(set1))

for x in dir(set1):
    if"_" not in x:
        print(x)
