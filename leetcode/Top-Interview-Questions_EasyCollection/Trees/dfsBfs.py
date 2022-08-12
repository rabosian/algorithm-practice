from collections import deque

def dfs(graph, v, visited):
    # set current node as visited
    visited[v] = True
    print(v, end=' ')
    # recursively visit nodes connected with current node
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    # set current node as visited
    visited[start] = True

    while queue:
        # pop current node from queue and print out 
        v = queue.popleft()
        print(v, end=' ')
        # append non-visited adjacent element to queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
