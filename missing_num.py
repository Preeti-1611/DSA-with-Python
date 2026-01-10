def MissingNum(nums):
    n = len(nums)
    total_sum = n*(n+1)//2
    array_sum = sum(nums)
    return total_sum - array_sum



nums = [3,4,2,1,6,7,8,0]
print(MissingNum(nums))


# Rule to remember (INTERVIEW GOLD ⭐)

# ✔️ Use n*(n+1)//2 ONLY WHEN

# Numbers are from 0 to n

# One number is missing

# No extra numbers

# ❓ Want to handle arrays like [3,4,2,1,6,7,8]?

# Then you must use a different logic (range-based or set-based).