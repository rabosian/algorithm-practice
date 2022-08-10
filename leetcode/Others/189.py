import timeit

start = timeit.default_timer()

def rotate(nums, k):
    # (i) O(n), Runtime: 0.503 ms
    # while k > 0:
    #     nums.insert(0, nums.pop()) # remove & insert
    #     k -= 1
    # return nums

    # (ii) l-k%l (remainder) 만큼 뒤로 보내기, using extend(), 0.308 ms
    # l-k is WRONG!!!, k could be larger than l
    rotate = k % len(nums) # actual rotate value
    remainder = len(nums) - rotate
    nums.extend(nums[:remainder]) # extend modifies original value
    del nums[:remainder]

    # (iii)
    # l = len(nums)
    # nums[:] = nums[l-k%l:] + nums[:l-k%l]


nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)

stop = timeit.default_timer()
print(f'Runtime: {round((stop - start)*1000, 3)} ms')