for i in "python":
    print("letter is :"+i)

list1=["cricket","football","kho-kho","baseball","hockey"]
for i in list1:
    print(i)

for i in list1:
    if i is "kho-kho":
        break
    print(i)

for i in list1:
    if i is "kho-kho":
        continue
    print(i)

for i in range(0,10,3):
    print(i)

dict1={"1":1,"2":2,"3":3,"4":4}
for i,j in dict1.items():
    print(i,"equals",str(j))


for i in range(1,11):
    for j in range(1,11):
        print("i*j",(i*j))
    print(" ")


#odd-even-------
for i in range(0,11):
    if i%2==0:
        print((i)," is even")
    else:
        print((i)," is odd")



#prime numbers------
print(2)
for i in range(3,20):
    div=False
    for j in range(2,i):
        if i%j==0:
            div=True
    if div==False:
        print(i)

