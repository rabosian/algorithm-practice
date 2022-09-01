def rotate(matrix):
    rows = [row for row in matrix]
    cols = list(zip(*matrix))
    for i in range(len(matrix)):
        cols[i] = list(reversed(cols[i]))
        matrix[i] = cols[i] 