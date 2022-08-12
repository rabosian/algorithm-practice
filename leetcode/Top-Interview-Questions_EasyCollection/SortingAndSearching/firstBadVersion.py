# bool isBadVersion(version) is a given API which returns boolean value whether version is bad

def firstBadVersion(n):
    start, end = 1, n
    while start <= end:
        mid = start + (end-start) // 2
        if isBadVersion(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start

