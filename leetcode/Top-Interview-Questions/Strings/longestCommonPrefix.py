def longestCommonPrefix(strs):
    result = ""
    if not strs:
        return result
    temp = list(zip(*strs))
    for i in range(len(temp)):
        if len(set(temp[i])) != 1:
            return result
        result += temp[i][0]
    return result

