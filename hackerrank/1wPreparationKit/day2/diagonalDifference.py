def diagonalDifference(arr):
    left, right = 0, 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[len(arr)-i-1][i]
    return abs(left-right)
    
    


