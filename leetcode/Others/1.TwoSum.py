
from tkinter import E


def twoSum(nums, target):
    stack = []
    for i in range(len(nums)):
        searchFor = target - nums[i]
        if searchFor in stack:
            return [nums.index(searchFor),i]
        else:
            stack.append(nums[i])


def twoSum_using_hashMap(nums, target):
    hashMap = {} # val: index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
    return -1

nums = [3,2,1,2,2,1]
target = 6
print(twoSum_using_hashMap(nums, target))

