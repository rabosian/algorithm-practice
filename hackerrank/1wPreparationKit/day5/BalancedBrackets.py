

def isBalanced(s):
    closingBrackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for char in s:
        if char in closingBrackets:
            if stack and stack[-1] == closingBrackets[char]:
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(char)
    return "YES" if not stack else "NO"
        

s = '{{}('
print(isBalanced(s))