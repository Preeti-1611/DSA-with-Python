# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def Twosum(num,target):

    n = len(num)

    freq_num = {}

    for i in range(0,n):
        remaining = target -num[i]
        if remaining in freq_num:
            return [freq_num[remaining],i]
        else:
            freq_num[num[i]] = i

num = [4,5,7,3,4,7]
target = 10
print(Twosum(num,target))


