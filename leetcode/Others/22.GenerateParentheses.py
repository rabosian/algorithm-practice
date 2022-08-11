def generateParenthesis(n):
    def generate(p, left, right, result=[]):
        if left:
            generate(p + '(', left-1,right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            result.append(p)
        return result

    return generate('', n, n)

# recursion 공부하기
n = 4
print(generateParenthesis(n))
