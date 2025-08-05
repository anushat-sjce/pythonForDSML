import numpy as np 
a = np.array([1,2])
b = np.array([3,4])

c = a + b
print(c)
print(type(c))



'''
Add function
'''

def addFunc(a, b):
    return a+b

X = 10
Y = 20
sum1 = addFunc(X,Y)
print("Sum : ", sum1)



'''
This module performs addition of 2 numbers
'''

def addFunc(a, b):
    return a + b

X = 10
Y = 20
k = addFunc(X,Y)
print("Sum :", k)
