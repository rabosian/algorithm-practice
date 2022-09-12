# find connected element
# N * M size of ice mold
# example input
# 4 5
# 00110
# 00011
# 11111
# 00000
# output: 3

# idea - dfs
# 1. check all directions of current node and visit them if their value is 0 and not visited yet.
# 2. set current node and repeat 1.
# 3. count non-visited nodes

# ver1
def dfs(x,y):
    # out of index
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # if not visit current node
    if graph[x][y] == 0:
        graph[x][y] = 1
        # call dfs of all directions
        dfs(x-1,y) # up
        dfs(x,y-1) # left
        dfs(x+1,y) # down
        dfs(x,y+1) # right
        return True
    return False

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1

# ver2
def iceCube(matrix):
    res = 0
    n = len(matrix)
    m = len(matrix[0])
    def dfs(x,y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if matrix[x][y] == 1:
            return False
        matrix[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                res += 1
    return res

matrix = [[1,0,1,1,1],
          [1,0,1,0,1],
          [1,1,1,0,1],
          [1,1,1,1,1]]

print(iceCube(matrix))