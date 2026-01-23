arr = [4, 6 , 33, 74, 92]
n = len(arr)

for i in range(n-1):
    is_swapped = False

    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            is_swapped = True

    if  is_swapped==False:
        break

print(arr)
