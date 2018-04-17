import numpy as np

def f(x):
    return 2 * x +3

def y(x):
    return x**2 


A = np.array([[1, 1, 1], 
             [1, 1, 1],
             [1, 1, 1]])


print(A)

B = np.dot(A, A)
B[2,2] = 10
print(B)