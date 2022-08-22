from collections import defaultdict


def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26 # a to z
        for char in s:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(s)
    return result.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))