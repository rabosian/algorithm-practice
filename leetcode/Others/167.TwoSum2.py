def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start < end:
        sum = numbers[start] + numbers[end]
        if sum == target:
            return [start + 1, end + 1]
        elif sum > target:
            end -= 1
        else:
            start += 1
        
# There are four ways to solve this problem.

# Dictionary: O(n) time and O(n) space
# This does not fulfill the constant space condition

# Brute Force: O(n^2) and O(1) space
# Quadratic runtime

# Binary search: O(nlogn) time and O(1) space
# Efficient but we can do it in linear time

# Two pointers: O(n) time and O(1) space
# Best of both worlds



numbers = [-1, 0]
target = -1

print(twoSum(numbers, target))