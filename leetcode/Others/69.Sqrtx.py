def mySqrt(x):
    if x < 1:
        return 0
    if x >= 1 and x < 4:
        return 1
        
    start, end = 2, x // 2
    mid = (start+end) //2
    while start <= end:
        if mid * mid > x:
            end = mid - 1
        else:
            start += 1
        mid = (start + end) // 2
    return mid

x = 6
print(mySqrt(x))