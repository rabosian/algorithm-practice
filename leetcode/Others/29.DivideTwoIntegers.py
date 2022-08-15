# Time limit exceed
def divide(dividend, divisor):
    result = 0
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    while dividend >= divisor and dividend != 0:
        dividend -= divisor
        result += 1

    result = -result if negative else result

    return min(max(-2147483648, result), 2147483647)


dividend = -2147483648
divisor = 1
print(divide(dividend, divisor))