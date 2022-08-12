def isPalindrome(s):
    stack = []
    for i in range(len(s)):
        if s[i].isdigit() or s[i].isalpha():
            stack.append(s[i].lower())
    return stack == stack[::-1]