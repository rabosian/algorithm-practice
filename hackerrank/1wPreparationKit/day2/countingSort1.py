def countingSort(arr):
    result = [0] * 100 
    # count the occurrence from 0 to 99
    for i in range(len(arr)):
        result[arr[i]] += 1
    return result    

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
print(countingSort(arr))