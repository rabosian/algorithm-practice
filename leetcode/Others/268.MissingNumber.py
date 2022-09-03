from time import process_time

def missingNumber(nums):
    shouldBe = [i for i in range(len(nums)+1)]
    # use extra space
    # return list(set(shouldBe)-set(nums))[0]

    for i in range(len(nums)):
        shouldBe.remove(nums[i])
    return shouldBe[0]

start_time = process_time()

nums = [3,0,1]
print(missingNumber(nums))

stop_time = process_time()

print(start_time)
print(stop_time)