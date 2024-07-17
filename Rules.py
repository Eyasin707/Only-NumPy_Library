#Let's learn NumPy Now:
#Day_01:

import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr2)
print(type(arr1)) #Object type
print(type(arr2))
print(arr2.ndim)  #Checking number of dimension

#accessing elements in ndarry:
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr1[2])
print(arr2[0,0])
print("The value in 3rd row and 3rd collumn:",arr3[2,2])
