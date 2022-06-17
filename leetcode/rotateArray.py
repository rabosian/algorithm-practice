def rotate(nums, k):
    rotate = k % len(nums) # 3
    remainder = len(nums) - rotate
    rotate = nums[remainder:]
    nums = nums[:remainder]
    


nums = [1,2,3,4,5,6,7]
k = 10
rotate(nums, k)
print(nums)