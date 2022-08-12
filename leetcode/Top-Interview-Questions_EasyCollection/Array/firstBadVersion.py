

def isBadVersion(version):
    if version == bad:
        return True
    else:
        return False

def firstBadVersion(n):
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end-start) //2
        if not isBadVersion(mid):
            start = mid + 1
        else:
            end = mid - 1
    return start

n = 7
bad = 5

print(firstBadVersion(n))