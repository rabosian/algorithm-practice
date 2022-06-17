def plusOne(digits):
    num = 0
    length = len(digits)
    for i in range(length):
        num += digits[i] * (10**(length-1-i))
    num += 1
    return [int(i) for i in str(num)]

digits = [1,2,9]
print(plusOne(digits))