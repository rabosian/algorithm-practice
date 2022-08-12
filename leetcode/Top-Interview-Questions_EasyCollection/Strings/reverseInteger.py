def reverse(x):
    s = str(x)
    if x < 0:
        result = int('-' + s[1:][::-1])
    else:
        result = int(s[::-1])
    return 0 if result < -pow(2,31) or result > pow(2,31) else result


x = 1534236469
print(reverse(x))