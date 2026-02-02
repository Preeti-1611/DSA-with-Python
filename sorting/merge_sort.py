def merge(left, right):
    result = []
    i = j = 0

    n = len(left)
    m = len(right)

    # Compare elements of both arrays
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy remaining elements of left array
    while i < n:
        result.append(left[i])
        i += 1

    # Copy remaining elements of right array
    while j < m:
        result.append(right[j])
        j += 1

    return result


def mergeSort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_half = mergeSort(left_arr)
    right_half = mergeSort(right_arr)

    return merge(left_half, right_half)



arr = [3,6,2,1,8,0,5]
print(mergeSort(arr))