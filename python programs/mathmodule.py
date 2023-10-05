import math as m

'''pi'''

print(m.pi)#returns pi number

'''e'''

print(m.e)#returns e number that natural logarithm

'''tau'''

print(m.tau)#returns ratio of a circle’s circumference to its radius. 

'''inf'''

print(m.inf)#returns positive infinity

'''nan'''
print(m.nan)#returns “not a number” (NaN) value

'''Ceil()'''

x=5.6

print(m.ceil(x)) #Returns the smallest integer greater than or equal to x

'''floor(x)'''

x=4.5

print(m.ceil(x))#Returns the largest integer less than or equal to x

'''fabs()'''

x=-4

print(m.fabs(x))#Returns the absolute value of x

'''factorial(x)'''

print(m.factorial(4))#returns factorial of number

'''fmod(x, y)'''

print(m.fmod(47,2))#Returns the remainder when x is divided by y

'''fsum(iterable)'''

l=[4,5,7,8]

print(m.fsum(l))#Returns an accurate floating point sum of values in the iterable

'''isfinite(x)'''

x=float('inf')

print(m.isfinite(x))#Returns True if x is neither an infinity nor a NaN (Not a Number)

'''exp(x)'''

print(m.exp(4))#Returns e**x

'''expm1(x)'''

print(m.expm1(4))#Returns e**x - 1

'''log(x[, base])'''

print(m.log(10))#Returns the logarithm of x to the base (defaults to e)

'''log2(x)'''

print(m.log2(10))#Returns the base-2 logarithm of x

'''pow(x, y)'''

print(m.pow(4, 4))#Returns x raised to the power y

'''sqrt(x)'''

print(m.sqrt(81))#Returns the square root of x

'''asin(x)'''

print(m.asin(m.sqrt(3)/2))#Returns the arc sine of x
#acos(x),atan(x) use same

'''sin(x)'''

print(m.sin(m.pi/2))#Returns the sine of x
#cos(x),tan(x) use same

'''asinh(x)'''

print(m.asinh(1/2))#Returns the inverse hyperbolic sine of x
#acosh(x),atanh(x) use same

'''sinh(x)'''

print(m.sinh(m.pi/2))#Returns the hyperbolic cosine of x
#cosh(x),tanh(x) use same