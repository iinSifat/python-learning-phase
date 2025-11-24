def reverse(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i], arr[j]= arr[j],arr[i]
        i+=1
        j-=1
#N:B: you can not write i++ or j-- in python

     
    return list

arr = ['apple', 'grape', 100, 3.4, [1, 2] , (2, 3)]
reverse(arr)
print(arr)