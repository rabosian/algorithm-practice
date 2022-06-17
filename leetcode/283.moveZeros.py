def moveZeros(nums):
    # Runtime 1329 ms
    # count = 0
    # while 0 in nums:
    #     nums.remove(0)
    #     count += 1
    
    # temp = [0] * count
    # nums.extend(temp)
    l = len(nums)
    nums[:] = [i for i in nums if i != 0] # 0 없는 array
    newList = len(nums)
    if nums != newList:
        nums[:] = nums + [0] * (l-newList)

            
nums = [0,1,3,0,12]
moveZeros(nums)
print(nums)