#descending order

def DesecSelection(num):
    n = len(num)
    for i in range(0,n):
        max_index = i
        for j in range(i+1,n):
            if num[j] >num[max_index]:
                max_index=j
        num[i],num[max_index] = num[max_index],num[i]

    return num
    
num =[3,5,6,8,9,2,1]
print(DesecSelection(num))
      

def AsenSelection(num):
    n = len(num)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if num[j] <num[min_index]:
                min_index=j
        num[i],num[min_index] = num[min_index],num[i]

    return num
    
num =[3,5,6,8,9,2,1]
print(AsenSelection(num))
      






