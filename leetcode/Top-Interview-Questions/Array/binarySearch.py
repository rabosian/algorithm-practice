def search(nums, target):
    if target not in nums:
        return -1
    return nums.index(target)

    # binary searching
    # first = 0
    # last = len(nums) - 1

    # while first <= last:
    #     mid = first + (last - first) // 2
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] > target:
    #         last = mid - 1
    #     else:
    #         first = mid + 1

      #  0 1 2 3 4 5
nums = [-1,0,3,5,9,12]
target = 9
result = search(nums, target)

print(result) # target index otherwise -1