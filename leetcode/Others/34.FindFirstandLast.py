def searchRange(nums, target):
    if not nums:
        return [-1,-1]
    start, end = 0, len(nums)-1
    while start <= end:
        if nums[start] == target and nums[end] == target:
            return [start, end]
        if nums[start] < target:
            start += 1
        if nums[end] > target:
            end -= 1
    return [-1,-1]



nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))
# return [3,4]