def rotate(matrix):
    rows = [row for row in matrix]
    cols = list(zip(*matrix))
    for i in range(len(matrix)):
        cols[i] = list(reversed(cols[i]))
        matrix[i] = cols[i] 



matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)
