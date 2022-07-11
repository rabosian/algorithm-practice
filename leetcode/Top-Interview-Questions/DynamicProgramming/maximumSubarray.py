def maxSubArray(nums):
    # for i in range(len(nums)):
    #     if nums[i-1] > 0:
    #         nums[i] += nums[i-1]
    # return max(nums)
    maxSum = -1e8
    currSum = 0

    for i in range(0, len(nums)):
        currSum = currSum + nums[i]
        if(currSum > maxSum):
            maxSum = currSum
        if(currSum < 0):
            currSum = 0
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))