# Truck Tour
from collections import deque


def truckTour(petrolpumps):
    queue = deque(petrolpumps)

    for i in range(len(queue)):
        cur = queue.popleft()
        moves = cur[0] - cur[1]
        if moves < 0:
            queue.append(cur)
            continue
        start = cur
        for j in range(len(queue)):
            cur = queue.popleft()
            moves += cur[0] - cur[1]

        if moves > 0:
            return petrolpumps.index(start)
    return -1


pair = [[1, 5], [10, 3], [3, 4]]
print(truckTour(pair))
