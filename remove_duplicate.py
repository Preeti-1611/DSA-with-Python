def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # index for unique elements

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


nums = [1,1,2,3,21,42,73,89,89]  # it should be sorted
print(remove_duplicates(nums))






















# def print_unique(nums):
#     if not nums:
#         return

#     print(nums[0], end=" ")

#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             print(nums[i], end=" ")
