list=["utkarsh","bondade",2,0,0,2]
print(list)
print(list[0])
list[3]=24
print(list)
print(len(list))
list.append("90")
print(list)
list.pop()
print(list)
list.remove("bondade")
print(list)
list.clear()
print(list)

for x in dir(list):
    if"_" not in x:
        print(x)