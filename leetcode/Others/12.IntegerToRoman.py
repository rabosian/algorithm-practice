def intToRoman(num):
    romanDict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'}

    if num in romanDict:
        return romanDict[num]
    result = ""
    index = 10 ** (len(str(num))-1)

    while num:
        cur = (num // index) * index
        num %= cur
        if cur in romanDict:
            result += romanDict[cur]
        elif cur < 4 * index: # 2 3
            while cur:
                result += romanDict[index]
                cur -= index

        elif cur < 9 * index: # 6 7 8
            result += romanDict[index * 5]
            cur -= index * 5
            while cur:
                result += romanDict[index]
                cur -= index
        
        while num and not num // index:
            index //= 10

    return result




num = 1994
print(intToRoman(num))
