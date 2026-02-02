# Function to reverse elements between start and end
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Function to rotate the array to the RIGHT by d positions
def rotate_right(arr, d):
    n = len(arr)
    
    # Handle cases where d > n
    

    # Step 1: Reverse the entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Step 3: Reverse the remaining elements
    reverse(arr, d, n - 1)


# Example
arr = [4,1,3,8,7]
rotate_right(arr, 2)
print(arr)