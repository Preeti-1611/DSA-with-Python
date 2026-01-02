# You are given an array of integers arr[]. You have to reverse the given array.

# Note: Modify the array in place.



def Reversearray(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left],arr[right]= arr[right],arr[left]
        left+=1
        right-=1
    
    return arr

arr = [4,5,3,7,5,8,4,2,0]
print(Reversearray(arr))