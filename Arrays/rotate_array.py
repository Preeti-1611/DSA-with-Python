def rotate_left(arr, d):
    n = len(arr)      # length of array

    d %= n            # handle d > n

    reverse(arr, 0, d-1)   # reverse first d elements
    reverse(arr, d, n-1)   # reverse remaining elements
    reverse(arr, 0, n-1)   # reverse whole array


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [3, 6, 2, 3, 4, 0, 5]
rotate_left(arr, 3)
print(arr)

