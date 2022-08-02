
# iterations = 0

# def cookies(k, A):
#     global iterations
#     A.sort()
#     if len(A) < 2:
#         return -1
#     A.append(1 * A[0] + 2* A[1])
#     A = A[2:]
#     iterations += 1
    
#     return iterations if all(elem >= k for elem in A) else cookies(k,A)

import heapq

def cookies(k, A):
    iterations = 0
    heapq.heapify(A)
    for i in range(len(A)):
        min1 = heapq.heappop(A)
        if min1 >= k:
            return iterations
        if len(A) == 0:
            return -1
        min2 = heapq.heappop(A)
        heapq.heappush(A, 1 * min1 + 2 * min2)
        iterations += 1


k = 8
A = [1, 2, 3, 9, 10, 12]
print(cookies(k,A))