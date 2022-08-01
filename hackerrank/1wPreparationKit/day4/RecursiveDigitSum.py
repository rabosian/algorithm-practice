def superDigit(n, k):
    if len(str(n)) == 1:
        return n
    sum = 0
    nums = list(str(n))
    for num in nums:
        sum += int(num)
    return superDigit(sum*k,1)


print(superDigit(9875,4))
