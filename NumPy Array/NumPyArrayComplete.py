
import numpy as np

arr = np.array([10,20,30,40])

print(arr)

print(type(arr))

print(arr[2])

print(arr[-3])

arr[0] = 100

print("Updated = ",arr)

print(arr[1:3])

print(arr.dtype)


#One Dimensional Array 

arrOf_1D = np.array([10,20,30,40,50])

print("1D Array ",arrOf_1D)

print(arrOf_1D.ndim)


arrOf_2D = np.array([
    [10,20,30],
    [40,60,70]
])

print("2D Array ",arrOf_2D)


print(arrOf_2D[0,1])

print(arrOf_2D.ndim)


arrOf_3D = np.array([
    [
        [1,2,3],
        [4,6,7]
    ],

    [
        [7,8,9],
        [10,11,12]
    ]
])

print("3D Array = ",arrOf_3D)

print(arrOf_3D.ndim)