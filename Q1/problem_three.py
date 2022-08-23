from __future__ import division
import math

# finally done 
# here is the catch
# you cant use inbuilt floor and ceil in this question as they dont give precise values at large values
# instead of that i had to make functions and to keep them as fast as possible
# took several attempts but i succeeded in the end :D

def ceil(a,b):
    if(a%b == 0):
        return a//b 
        #this division rounds up the value to an integer and works more efficient than hard division
    return a//b + 1


def ilog(x,y):
    # this function evaluates the ceiling of the logarithm of x on base 2
    ans = 0
    floor = False
    while(x!=1):
        if(x%y != 0):
          floor = True
        x=x//y
        ans+=1
    if(floor):
        return ans + 1
    return ans    

def flog(x):
    #this function evalutates the floor of the logarithm of x on base 2
    y = x
    return y.bit_length() - 1 
        
        
    



t = int(input())
 
while t>0:
    str = input()
    arr = str.split()
    n = int(arr[0])
    k = int(arr[1])
    s = 2**(flog(k) + 1)
    # at the starting the computers will double until the point when cable will be unsufficient
    # after that the computers will increase by k each hour
    if(n <= s):
        print((ilog(n,2)))
    elif k==1:
        print(n-1)    
    else:
        print(ceil(n-s,k) + flog(k) + 1)

    
 
    t= t-1