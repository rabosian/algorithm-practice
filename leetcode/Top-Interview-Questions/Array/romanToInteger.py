
# time complexity = O(N) -> single loop
# space complexity = O(1) -> hash map
def romanToInt(s):
    romanDict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000 }
    result = 0

    for i in range(len(s)-1):
        if romanDict[s[i]] < romanDict[s[i+1]]:
            result -= romanDict[s[i]]
        else:
            result += romanDict[s[i]]

    result += romanDict[s[-1]]
    return result

s = "CMXCVIII"
print(romanToInt(s))