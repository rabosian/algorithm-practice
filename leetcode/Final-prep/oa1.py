def Search(strArr):
    res = 0
    row = len(strArr)
    col = len(strArr[0])

    def dfs(x, y):
        # out of boundary
        if x < 0 or y < 0 or x >= row or y >= col:
            return False
        if strArr[x][y] == "0":
            strArr[x][y] = "1"
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False

    for i in range(len(strArr)):
        strArr[i] = list(strArr[i])

    for i in range(row):
        for j in range(col):
            if dfs(i, j) == True:
                res += 1

strArr = ["01111", "01101", "00011", "11110"]
print(Search(strArr))
