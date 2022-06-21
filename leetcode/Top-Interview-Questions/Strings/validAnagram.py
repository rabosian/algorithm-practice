from collections import Counter

def isAnagram(s, t):
    # (i) Using collections.Counter 
    # sDict = Counter(s)
    # tDict = Counter(t)
    # if sDict & tDict == sDict:
    #     return True
    # return False

    # (ii) Using Dictionary
    sDict, tDict = {}, {}
    for i in range(len(s)):
        if s[i] not in sDict:
            sDict[s[i]] = 1
        else:
            sDict[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in tDict:
            tDict[t[i]] = 1
        else:
            tDict[t[i]] += 1

    return True if sDict == tDict else False
