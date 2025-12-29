arr = [34,7,2,39,39]


largest = float('-inf')
second_largest = float('-inf')

for  x  in arr:
    if x >largest:
        second_largest = largest
        largest = x
    elif  x < largest and x > second_largest :
          second_largest = x
        
print("the second largest number",second_largest)



def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # finding the second largest element
    for i in range(n):

        # If arr[i] > largest, update second largest with
        # largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
      
        # If arr[i] < largest and arr[i] > second largest, 
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))














    # class Solution:
    # def getSecondLargest(self, arr):
    #     # Code Here
        
    #     n = len(arr)
        
    #     largest = -1
    #     second_largest = -1
        
        
    #     for i in range(n):
    #         if arr[i] >largest:
    #             second_largest = largest
    #             largest = arr[i]
                
    #         elif arr[i] !=largest and arr[i] >second_largest:
    #               second_largest = arr[i]
                  
                  
    #     return second_largest 