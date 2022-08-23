from operator import truediv


t = int(input())
while t>0:
    n = int(input())
    isFalse = True
    name = input()
    arr = name.split()
    # splitting array then sorting it to reduce time complexity
    arr.sort()
    for x in range(0,n-2):
        if(arr[x]==arr[x+1] and arr[x+1]==arr[x+2]):
            print(arr[x])
            isFalse = False
            break
    if(isFalse):
        # if there is no such element then -1 will be printed
        print(-1)    
    t=t-1
