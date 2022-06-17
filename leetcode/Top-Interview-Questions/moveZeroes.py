def moveZeros(nums):
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)
    



nums1 = [0,1,0,3,12]

moveZeros(nums1)
print(nums1)