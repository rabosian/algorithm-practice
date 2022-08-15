# must write with O(logN) time complexity
def search(nums, target):
    start, end = 0, len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
            
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        else:
            if nums[mid] <= target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1


nums = [3,1,2]
target = 2
print(search(nums, target))