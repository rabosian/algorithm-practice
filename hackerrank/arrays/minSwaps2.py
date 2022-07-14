
def swapPos(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

def minimumSwaps(arr):
    swap = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i]-1 # arr.index(i+1) is O(n^2)
            arr[i], arr[temp] = arr[temp], arr[i]
            print(arr)
            swap += 1
        
    return swap


arr = list(map(int, input().split()))
res = minimumSwaps(arr)
print(res)
