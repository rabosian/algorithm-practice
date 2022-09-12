# N * M size of maze
# blocks: 0, roads: 1
# determine minimum moves (including start, end point) to escape given maze
# example input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# output: 10

# idea - bfs
# 1. check adjacent nodes of current node and visit them if their value is 1 and not visited yet.
# 2. set current node and repeat 1.
# 3. count non-visited nodes

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # check 4 directions (NSWE)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # out of graph
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # ignore blocks
            if graph[nx][ny] == 0 or (nx,ny) == (0,0):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#      N S  W E
dx = [-1,1, 0,0]
dy = [0, 0,-1,1]

print(bfs(0,0))