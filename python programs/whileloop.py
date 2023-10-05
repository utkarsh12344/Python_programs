num1=1
while num1<10:
    print(num1)
    num1+=1

num2=5
while num2<10:
    if num2==7:
        break
    print(num2)
    num2+=1


num3=5
while num3<9:
    num3+=1
    if num3==7:
        continue
    print(num3)