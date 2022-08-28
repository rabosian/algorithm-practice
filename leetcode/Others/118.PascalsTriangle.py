def generate(numRows):
    result = [[1]]
    for i in range(numRows-1):
        temp = [1]
        prev = result[-1]
        for j in range(len(prev)-1):
            temp.append(prev[j] + prev[j+1])
        temp.append(1)
        result.append(temp)
    return result


numRows = 5
print(generate(numRows))