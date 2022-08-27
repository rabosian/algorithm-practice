
def canJump(nums):
    maxReach = 0
    for i, n in enumerate(nums):
        if i > maxReach:
            return False
        if maxReach >= len(nums)-1:
            return True
        maxReach = max(maxReach, i + n)

nums = [3,2,1,1,4]
print(canJump(nums))