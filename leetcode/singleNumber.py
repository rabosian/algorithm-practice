from collections import Counter

def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]

    myDict = Counter(nums)
    
    for key, value in myDict.items():
        if value == 1:
            return key
    


nums = [4,4,8,8,2]
print(singleNumber(nums))