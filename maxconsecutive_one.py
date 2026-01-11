def max_consecutive_one(num):
    count =0 
    max_count = 0

    for i in range(0,len(num)):
        if num[i]==1:
            count+=1
        else:
            max_count = max(max_count,count)
            count =0
  

    return max(max_count,count)


num = [0,1,1,1,0,1,0,0,1,1,1,1,1]

print(max_consecutive_one(num))