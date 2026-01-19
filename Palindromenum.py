def isPalindrome(num):
    x = num
    result = 0
    while x >0 :
        last = x%10
        result = result*10+last
        x = x//10
    
    return num == result


num = 1211
print(isPalindrome(num))