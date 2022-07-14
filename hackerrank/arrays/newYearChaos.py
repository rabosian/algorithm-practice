def minimumBribes(q):
    result = 0
    p1 = 1
    p2 = 2
    p3 = 3
    for i in range(len(q)):
        if q[i] == p1: # 1 2 3
            p1 = p2
            p2 = p3
            p3 += 1
        elif q[i] == p2: # 2 1 3 => next check 1 3 4
            result += 1
            p2 = p3
            p3 += 1
        elif q[i] == p3: # 3 1 2 => next check 1 2 4
            result += 2
            p3 +=1
        else:
            print("Too chaotic")
            return
    print(result)



########
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
