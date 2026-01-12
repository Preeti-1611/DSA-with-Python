def rearrange(num):
    n = len(num)
    result =[0]*n
    pos_index,neg_index = 0,1
    for i in range(0,n):
        if num[i]>=0:
            result[pos_index]=num[i]
            pos_index+=2
        else:
            result[neg_index]=num[i]
            neg_index+=2
    return result

num = [3,0,-4,-7,2,4,-5]
print(rearrange(num))
