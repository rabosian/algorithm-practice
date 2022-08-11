def letterCombinations(digits):
    if not digits:
        return []
    lettersDict = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    if len(digits) == 1:
        return list(lettersDict[digits])

    result = ['']
    for i in range(len(digits)):
        result = [prev + l for prev in result for l in lettersDict[digits[i]]]
    return result



digits = "234"
print(letterCombinations(digits))
