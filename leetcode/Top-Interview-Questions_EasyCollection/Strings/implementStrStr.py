def strStr(haystack, needle):
    if needle == "": return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    else:
        return -1

