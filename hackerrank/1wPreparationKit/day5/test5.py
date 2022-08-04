# pairs
def pairs(k, arr):
    result = 0
    if k == 0 or len(arr) == 0:
        return result
    arr.sort()
    slow, fast = 0, 1
    while fast < len(arr):
        if arr[fast] - arr[slow] < k:
            fast += 1
        elif arr[fast] - arr[slow] > k:
            slow += 1
        else:
            result += 1
            fast += 1
    return result



print(pairs(3,[1,3,2,4,6,7]))