from collections import Counter


def minWindow(s, t):
    if len(t) > len(s):
        return ""
        
    tCount, sCount = Counter(t), Counter()
    start, end = 0, 0  
    options = []
    while end <= len(s)-1:
        sCount[s[end]] += 1
        end += 1
        if sCount & tCount != tCount:
            continue
        
        while start < end:
            sCount[s[start]] -= 1
            start += 1
            if sCount & tCount == tCount:
                continue
            options.append(s[start-1:end])
            break
    
    return min(options, key=len) if options else ""
    

s = "a"
t = "a"
print(minWindow(s,t))