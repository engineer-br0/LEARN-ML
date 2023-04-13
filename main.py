import numpy as np

arr = np.array([[3, 4, 5],[6,7,8]])
arr2 = np.array([[3, 4, 5],[6,7,8]])
#print(arr.dtype)
#print(arr.shape)

# print(np.zeros((4,5), dtype='int32')) // np.ones // np.empty

# SLICING '''
# arr2 = arr[1 : 3].copy()
# arr2[0] = 9
# print(arr)


#print(arr.sum(axis = 1))
arr = arr.reshape(3,2)
print(arr)
