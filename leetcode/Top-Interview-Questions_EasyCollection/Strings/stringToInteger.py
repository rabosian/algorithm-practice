def myAtoi(s):
    temp = s.strip()
    if len(temp) == 0: return 0
    
    sign = -1 if temp[0] == '-' else 1
    if temp[0] in '-+': temp = temp[1:]
    result = 0
    for c in temp:
        if not c.isdigit():
            break
        result = result*10 + int(c)

    return max(-pow(2,31), min(sign*result, 2**31-1))

