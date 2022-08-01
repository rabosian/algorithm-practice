def minimumBribes(q):
    bribes = 0
    swaps = [1,2,3]
    for i in range(len(q)):
        if q[i] == swaps[0]:
            swaps.append(swaps[2]+1)
            swaps.pop(0)
        elif q[i] == swaps[1]:
            swaps.append(swaps[2]+1)
            swaps.pop(1)
            bribes += 1
        elif q[i] == swaps[2]:
            swaps[2] += 1
            bribes += 2
        else:
            print("Too chaotic")
            return
    print(bribes)


q = [2,5,1,3,4]
minimumBribes(q)
