import random as r

'''random()'''

print(r.random())# returns between 0 and 1, including 0; but not including 1 [0,1)

'''randint(a, b)'''

print(r.randint(4,10))#returns integer value between [4,10] this mean include 4 and 10

'''randrange(start, stop[, step])'''

print(r.randrange(0,8,2))#Returns a number that is not included in the max in the min and max range
#first parameter is start point, second parameter is stop point, last parameter is step amount

'''sample(list,q)'''

numbers=range(50)

print(r.sample(numbers,7))#In the list, q returns the random value.

'''Choice'''

l=[1,2,3,4,5,6,7,8,9,10,11,12]

x=r.choice(l)

print(x)#choice one eleman that created list and returns

'''Shuffle'''

l=[4,5,6,7,8,9,10,11,12,12,14,15]

x=r.shuffle(l)

print(l)#changes the order of elements in the created list

'''uniform(a, b)'''

print(r.uniform(0, 9))#Return a random floating point number between a and b inclusive
