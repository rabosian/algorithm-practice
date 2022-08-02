from collections import deque

t = int(input())  # number of queue
queue = []

for i in range(t):
    query = list(map(int, input().split()))
    if (query[0] == 1):
        queue.append(query[1])
    elif (query[0] == 2):
        queue.pop(0)
    elif (query[0] == 3):
        print(queue[0])

# using deque
queue = deque()

for i in range(t):
    query = list(map(int, input().split()))
    if (query[0] == 1):
        queue.append(query[1])
    elif (query[0] == 2):
        queue.popleft()
    elif (query[0] == 3):
        print(queue[0])
