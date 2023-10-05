#A lambda function can take any number of arguments, but can only have one expression.

#lambda function seems function but it is easy and fast.
mult=lambda x,y: x*y

print(mult(15,10))

print("******************************************************************")
#factorial calculator with using lambda 
fact = lambda x: 1 if x == 0 else x * fact(x-1)

print(fact(5))

print("******************************************************************")

#square calculation of number with using lambda 
square=lambda x: x*x

print(square(7))