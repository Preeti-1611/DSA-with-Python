def rightrotate(num,k):
     n = len(num)
     k%=n

     reverse(num,0,n-1)
     reverse(num,k,n-k)
     reverse(num,0,k-1)

    

def reverse(num,left,right):
       while left<right:
             num[left],num[right] = num[right],num[left]
             left+=1
             right-=1
             return num

num = [4,6,3,2,3]
k =2
print(rightrotate(num,k))