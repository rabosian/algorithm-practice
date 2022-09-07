def uniquePaths(m,n):
    # m: rows, n: cols => matrix[m][n]
    if m or n == 1:
        return 1
    if m or n == 2:
        return m if m == 2 else n
