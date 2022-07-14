p = 5
# q = [1,2,5,3,7,8,6,4]
# q = [5,1,2,3,7,8,6,4]

q = [2,1,5,3,4]
q = [i-1 for i in q]
moves = 0
print(list(enumerate(q)))

for i,p in enumerate(q):
    if p-i > 2:
        print("Too chaotic")
        break
    
    for j in range(max(p-1,0), i):
        if q[j] > p:
            moves += 1
print(moves)
