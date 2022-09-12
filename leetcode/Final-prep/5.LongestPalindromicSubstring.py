def getPalindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


def longestPalindrome(s):
    if s == s[::-1]:
        return s
    p = ""
    for i in range(len(s)):
        p1 = getPalindrome(s, i, i+1) # even
        p2 = getPalindrome(s, i, i) # odd
        p = max([p,p1,p2], key=lambda x: len(x))
    return p



print(longestPalindrome("cbbcbcd"))
