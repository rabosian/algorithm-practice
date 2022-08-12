
def twoSum(nums, target):
    stack = []
    for i in range(len(nums)):
        searchFor = target - nums[i]
        if searchFor in stack:
            return [nums.index(searchFor),i]
        else:
            stack.append(nums[i])



nums = [3,2,1,2,2,4]
target = 6
print(twoSum(nums, target))

