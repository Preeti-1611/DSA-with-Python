

def containsDuplicate(nums):
    
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums =[3,2,1,2,4]
print(containsDuplicate(nums))
            