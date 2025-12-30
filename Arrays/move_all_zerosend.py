def Allzeroend(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

    return arr


arr = [3, 5, 0, 4, 0, 2]
print(Allzeroend(arr))
