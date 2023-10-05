
'''NumPy is the basic package used in Python for 
scientific calculations.It seeems like Matlab. 
It is a Python library that enables us to process
operations on arrays, including multidimensional 
arrays, various derived objects (such as masked 
arrays and matrices) and lots of mathematical, 
logical, shape manipulation, sorting, selection, 
discrete Fourier. Statistical operations and
simulations can be done using NumPy. NumPy 
library with C ++ does not cause any loss of
 performance.'''

import numpy as np #import numpy library as np

'''Intro'''

array=np.array([1,2,3,4])#create numpy array

print(array)

print(type(array))

print(array.shape)#returns type of matris that mean how many rows and how many columns  

print(array[0])#Access any eleman using list method in numpy array

array[2]=12 #Change an element of the array

print(array)#print new array on the screen

print("******************************************************************")

'''Some important methods that give information of array '''

array2=np.array([[12,23,14],[25,36,78]]) #create 2 dimension array

print(array2)

print(array2.shape) 

print(array2.ndim)#returns dimension of array

print(array2.size)#returns size of array how many number or eleman include in array

print(array2.dtype)# returns data type of array.Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

print(array2.itemsize)#the size in bytes of each element of the array. 

print("******************************************************************")

'''Create some types arrays in Numpy'''

print(np.zeros(5))  # Create an array of all zeros

print(np.zeros((2,3)))#2 dimension zeros array

print(np.ones((4,4))) # Create an array of all ones

print(np.full((3,3), 3)) # Create a constant array

print(np.eye(2))#identity array

print(np.empty([4, 2],dtype=int)) #we decide data type of array also empty function create random number in matrix

print(np.arange(3,7)) #returns an array that between start point to stop point.

print(np.linspace(5.0,7.0, num=5))#returns an array that split n point between start point to stop point

print(np.random.rand(2,2))

print("******************************************************************")

'''Basic Operations'''
a=np.array([1,4,7])
b=np.array([2,5,8])

summation=a+b
subtraction=a-b

mult=a*b # elementwise product
mult1=a@b # matrix product
mult2=a.dot(b) # another matrix product

mult3=a*5 
mult4=10*np.sin(b) 

div=a/b
square=np.sqrt(a)

boolean=a>1

x=a.sum()#returns summation of each element
y=a.min()#returns minimum element of a matris
z=a.max()#returns maximum element of a matris


print(summation)
print(subtraction)
print(mult)
print(mult1)
print(mult2)
print(mult3)
print(mult4)
print(div)
print(square)
print(boolean)
print(x)
print(y)
print(z)

print("******************************************************************")

newArray=np.array([[12,24,25],[21,47,65]])

print(np.sum(newArray, axis=0)) # Compute sum of each column
print(np.sum(newArray,axis=1)) # Compute sum of each row

print("******************************************************************")

'''Universal Functions'''

array3=np.array([1,2,3,4,5,6,7,8,9])

print(np.mean(array3))#returns the average of the array elements.

print(np.median(array3))#Returns the median of the array elements.

print(np.std(array3))#Returns the standard deviation, a measure of the spread of a distribution, of the array elements.****std = sqrt(mean(abs(x - x.mean())**2)).***

print(np.sort(array3))#returns sorted matris

print(np.transpose(array3))#returns tranpose of matrix

print(np.var(array3))#Returns the variance of the array elements, a measure of the spread of a distribution. ***var = mean(abs(x - x.mean())**2).***

print(np.cumsum(array3))#Return the cumulative sum of the elements along a given axis.

print("******************************************************************")

'''Indexing, Slicing'''

array4=np.array([0,1,8,27,64,125,216,343,512,729])

print(array4[5])

print(array4[3:7])

print(array4[: : -1])  # reversed array4

#for loop

for i in array4:
    print(i**2)#returns square of each eleman
    
    
array5 = np.array([[1, 2], [3, 4]])

for index, x in np.ndenumerate(array5):
     print(index, x)
    

        
print("******************************************************************") 

'''Shape Manipulation'''

array6=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(array6.shape)

print(array6.ravel())#returns flattened array

print(array6.reshape(6,2))#returns 6x2 matris 

#Several arrays can be stacked together along different axes
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print(np.hstack((a,b)))#x axis

print(np.vstack((a,b)))#y axis

print("******************************************************************") 

'''Copies'''

c=a.copy()

print(c)

c[0,1]=148

print(a[0,1])

print(c[0,1])

print("******************************************************************") 

'''End of Numpy Thank you'''
'''Next Topic is Pandas...'''