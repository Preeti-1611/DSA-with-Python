def RemoveElement(num,val):
    i =0
    while i <len(num):
        if num[i] ==val:
            num[i],num[-1]=num[-1],num[i]
            num.pop()

        else:
            i+=1
    
    return num

num = [2,3,3,2,2,2]
print(RemoveElement(num,3))
