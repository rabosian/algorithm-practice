# Palindrome Index
def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        temp = s[:i] + s[i+1:]
        if temp == temp[::-1]:
            return i
    else:
        return -1


s = "bcbc"
print(palindromeIndex(s))
