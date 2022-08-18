def permute(nums):
    if len(nums)==1:
        return [nums[:]]
    
    result = []
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        print(perms)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
        
    return result
    

print(permute([1,2,3]))