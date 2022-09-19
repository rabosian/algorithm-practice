def exist(board, word):
    n, m = len(board), len(board[0])
    def dfs(x,y,i):
        if i == len(word):
            return True
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if board[x][y] != word[i]:
            return False

        temp, board[x][y] = board[x][y], "@"
        res = (dfs(x-1,y,i+1) or dfs(x+1,y,i+1) or
                dfs(x,y-1,i+1) or dfs(x,y+1,i+1))
        board[x][y] = temp
        return res

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0] and dfs(i,j,0) == True:
                return True
    return False


board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]

word = "ABCES"
print(exist(board, word))