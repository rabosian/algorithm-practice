def getPalindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


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
