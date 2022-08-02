t = int(input())  # number of queue
s = ""
revert = []

for i in range(t):
    query = input().split()
    if (query[0] == '1'):
        revert.append(s)
        s += query[1]

    elif (query[0] == '2'): # remove last k char
        revert.append(s)
        s = s[:len(s)-int(query[1])]

    elif (query[0] == '3'): # print kth char
        print(s[int(query[1])-1])

    elif (query[0] == '4'): # undo
        s = revert.pop()

        