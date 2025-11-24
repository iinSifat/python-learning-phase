import numpy as np
r = int(input("rows:"))
c = int(input("colums:"))
arr = np.zeros((r,c), dtype = int)
for i in range(r):
    for j in range (c):
        arr[i][j] = int(input())
        
print("Initial array:")
print(arr)
arr = np.reshape(arr, (1, r*c))
print("Reshaped array:")
print(arr)
