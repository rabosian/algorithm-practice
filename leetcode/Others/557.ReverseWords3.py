def reverseWords(s):
    
#   Let's, take, LeetCode, contest
    s = s.split()
    for i in range(len(s)):
         s[i] = s[i][::-1]
    return ' '.join(s)




    # words = s.split()
    
    # for i in range(len(words)):
    #     chars = list(words[i])
    #     start = 0
    #     end = len(chars)-1
    #     while start < end:
    #         chars[start], chars[end] = chars[end], chars[start]
    #         start += 1
    #         end -= 1
    #     words[i] = ''.join(chars)

    # return ' '.join(words)
        


s = "Let's take LeetCode contest"
print(reverseWords(s))