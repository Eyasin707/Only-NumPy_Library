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

#slicing:
arr1 = np.array([1,2,3,4,5])
print(arr1[:4])
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[1,:3])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3[0,2:])

#data type:
print(arr2.dtype)
new_format=arr2.astype(bool)
print(new_format)

import numpy as np
arr1= np.array([1,2,3,4,5,6,7,8,9])
filt_arr= arr1%2==0
new_arr=arr1 [filt_arr]
print(new_arr)

import numpy as np
arr1= np.array([1,2,3,4,5,6,7,8,9])
fil_arr=[]

for element in arr1:
    if element%2==0:
        fil_arr.append(True)
    else:
        fil_arr.append(False)
new_arrr= arr1[fil_arr]
print(new_arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

