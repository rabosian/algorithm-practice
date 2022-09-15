
# create hash map
# if closing parenthesis matches opening parentheses
# check backward
# open = ['(', '[', '{']
# close = [')', ']', '}'] XXXXX
# HASH MAP !!
def isValid(s):
    stack = []
    closeToOpen = { ')':'(', ']':'[', '}':'{'} 
    
    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


    
s = "{{[]}[[[]]]}"
print(isValid(s))



