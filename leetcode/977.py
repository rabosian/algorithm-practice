import timeit

start = timeit.default_timer()


def sortedSquares(nums):
    # using O(n) & sorted()
    # Runtime:  0.00055
    # for i in range(len(nums)):
    #     nums[i] *= nums[i]
    
    # return sorted(nums)

    # using two-pointer
    # Runtime:  0.00028
    # TODO 1. set pointer to both ends and set index of result to the end
    start, end = 0, len(nums) -1
    result = [0] * len(nums) # same length with nums consist of 0
    index = len(nums) - 1
    # TODO 2. compare their absolute value and move pointer respect to result
    # TODO 3. append high value to the end of result array (or opposite)
    while start <= end:
        if abs(nums[start]) <= abs(nums[end]):
            result[index] = nums[end] ** 2
            end -= 1
        else:
            result[index] = nums[start] ** 2
            start += 1
        index -= 1
    return result


nums = [-7,-3,-1,2,3,11]
print(sortedSquares(nums))

stop = timeit.default_timer()
print('Runtime: ', stop - start)
