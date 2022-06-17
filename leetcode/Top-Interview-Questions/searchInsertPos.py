
def searchInsert(nums, target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return start




#       0 1 2 3
nums = [1,3,5,6]
target = 4 # output = index 1 supposed position
print(searchInsert(nums, target))