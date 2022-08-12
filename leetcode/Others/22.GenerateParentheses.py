def generateParenthesis(n):
    def generate(p, left, right, result=[]):
        if left:
            print(p)
            generate(p + '(', left-1,right)
        if right > left:
            print(p)
            generate(p + ')', left, right-1)
        if not right:
            result.append(p)
        return result

    return generate('', n, n)


n = 2
print(generateParenthesis(n))
