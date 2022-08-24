
def spiralOrder(matrix):
    result = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:
        # i in every top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        # i in every top right
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # i in every bottom row
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        bottom -= 1
        # i in every bottom left
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1

    return result


matrix = [[1], [2], [3], [4]]
print(spiralOrder(matrix))
