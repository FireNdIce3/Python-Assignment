# palindrome function
def is_palindrome(s):
    return s == s[::-1] 
    # s[::-1] gives the whole string in reverse format


t = int(input())
while t>0:
    name = input()
    i=0
    isFalse = True
    length = len(name)
    # there are two possibilities when the 1st or the last gives no palindrome 
    if(is_palindrome('a' + name) == False):
        isFalse = False
        print("YES")
        print('a' + name)
            
    elif(is_palindrome(name + 'a')== False):
        isFalse = False
        print("YES")
        print(name + 'a')
        
    if isFalse:
        print("NO")    
    t=t-1        



