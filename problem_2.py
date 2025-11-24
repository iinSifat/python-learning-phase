n = input()
print(n)
#isdigit returns true when each character  of the string is a digit
res=0
if n.isdigit():
    n = int (n)
    count=0
    
    if n%2!=0:
        for i in range(1,n+1,2):
            res+=(i*i)
            
    elif n%2==0:
        for i in range(1,n+2,2):
            res+=(i*i)
            count+=1
            
    print(res)

else:
    print("error")
