def threeSum(nums):
    result = []
    nums.sort()
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return result

    for i in range(len(nums)):
        target = 0 - nums[i]
        if i > 0 and nums[i] == nums[i-1]:
            continue

        start, end = i+1, len(nums) - 1  # start = i + 1 !!!
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                result.append([nums[i], nums[start], nums[end]])
                while start + 1 < len(nums) and nums[start] == nums[start+1]:
                    start += 1
                start += 1
                end -= 1
    return result


nums = [0,0,0]
print(threeSum(nums))
