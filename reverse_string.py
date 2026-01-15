def ReverseString(s):
    n = len(s)
    left =0
    right =n-1

    for i in range(0,n):
        if left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        

    return s


    
s=['h','e','l','l','o']
print(ReverseString(s))