
def removeDuplicates(nums):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    length = len(nums)
    nums = nums[:k+1]
    underscores = ['_'] * (length - k - 1)
    nums.extend(underscores)
    return k+1

# 0 1 2 3 4
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
