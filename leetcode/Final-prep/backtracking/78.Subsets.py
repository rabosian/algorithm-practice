def subsets(nums):
    res = []
    temp = []
    def dfs(i):
        if i >= len(nums):
            res.append(temp[:])
            return
        temp.append(nums[i])
        dfs(i+1)
        temp.pop()
        dfs(i+1)
    dfs(0)
    return res


nums = [1,2,3]
print(subsets(nums))