def lengthOfLongestSubstring(s):
    # result = ""
    # words = []
    # if len(set(s)) == 1:
    #     return 1

    # for i in range(len(s)):
    #     if s[i] in result:
    #         words.append(result)
    #         if s[i] != result[-1]:
    #             index = result.index(s[i])
    #             result = result[index+1:]
    #         else:
    #             result = ""
    #     result += s[i]
    # words.append(result)
    # return len(max(words, key=len))
    
# 이걸로도 풀어보기 
    # start = maxLength = 0
    # usedChar = {}
    
    # for i in range(len(s)):
    #     if s[i] in usedChar and start <= usedChar[s[i]]:
    #         start = usedChar[s[i]] + 1
    #     else:
    #         maxLength = max(maxLength, i - start + 1)

    #     usedChar[s[i]] = i


s = "dvdf"
print(lengthOfLongestSubstring(s))