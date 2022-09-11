from itertools import combinations


def subsets(nums):
    res = [[]]
    if len(nums) == 1:
        res.append(nums)
        return res

    for i in range(1,len(nums)+1):
        res.extend(combinations(nums, i))
    return res


nums = [1,2,3]
print(subsets(nums))