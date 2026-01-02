# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.





def rotate_left(arr, d): #right rotate
    n = len(arr)      # length of array

    d %= n                # Handle the case where d > size of array

    reverse(arr, 0, d-1)   # reverse first d elements
    reverse(arr, d, n-1)      # Reverse the remaining n-d elements
    reverse(arr, 0, n-1)   # reverse whole array


# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [3, 6, 2, 3, 4, 0, 5]
rotate_left(arr, 3)
print(arr)


#############################################################################3

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
    d = d % n

    # Step 1: Reverse the entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Step 3: Reverse the remaining elements
    reverse(arr, d, n - 1)


# Example
arr = [1, 2, 3, 4, 5, 6, 7]
rotate_right(arr, 2)
print(arr)
