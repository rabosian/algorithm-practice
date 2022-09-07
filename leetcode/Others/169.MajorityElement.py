from collections import Counter

def majorityElement(nums):
    if len(nums) == 1:
        return nums[0]
    
    majority = len(nums) / 2
    counts = Counter(nums)
    
    for key in counts:
        if counts[key] > majority:
            return key

nums = [3,2,3,1,1,1,2,2,2,2,2]
print(majorityElement(nums))