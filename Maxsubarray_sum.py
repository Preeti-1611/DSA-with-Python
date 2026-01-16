def Maxsubarray(nums):

        n = len(nums)
        maxi = float("-inf")
        total =0
        for i in range(0,n):
            total = total+nums[i]
            maxi = max(maxi,total)
            if total <0:
                total = 0
       
       
        return maxi

nums =[-3,4,-7,2,0,-2,5,3]
print(Maxsubarray(nums))