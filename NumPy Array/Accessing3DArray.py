
import numpy as np 

arr = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],

    [
        [7,8,9],
        [10,11,12]
    ],

    [
        [13,14,15],
        [16,17,18]
    ]
    ])

print(arr)

print(arr.ndim)

print(arr[2,1,2])

print(arr[1,0,1])

print(arr[2,1,:])

print(arr[0,:,2])

print(arr[:,0,:])

print(arr[:,:,2])

