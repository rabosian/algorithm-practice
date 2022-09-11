def uniquePaths(m,n):
    if m == 1 or n == 1:
        return 1
    # row = [i for i in range(1,n+1)]
    row = [1] * n
    for i in range(m-1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    return row[0]

print(uniquePaths(3,5))
