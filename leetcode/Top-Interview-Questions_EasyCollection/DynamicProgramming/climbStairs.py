def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 0
    for _ in range(n):
        a, b = a + b, a
        print(f"a: {a}")
    return a
