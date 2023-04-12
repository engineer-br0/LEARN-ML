import numpy as np

arr = np.array([3, 4, 5])

#print(arr.dtype)
#print(arr.shape)

# print(np.zeros((4,5), dtype='int32')) // np.ones // np.empty

arr2 = arr[1 : 3].copy()
arr2[0] = 9
print(arr)