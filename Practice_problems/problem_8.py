import numpy as np
#arr = np.random.randint(0, 10, (3,3))
arr = np.array([[6,3, 6],
 [7 ,2 ,7],
 [5, 0 ,6]])
print(arr)
print("Slicing the last two row:")
arr2 = arr[1:3,:]
print(arr2) #3 exlusive
sum = 0
print(arr2.shape)
row, col = arr2.shape
for i in range (row):
    for j in range (col):
        sum += arr2[i][j]

print("sum", sum)