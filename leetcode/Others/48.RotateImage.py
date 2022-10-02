# def rotate(matrix):
#     rows = [row for row in matrix]
#     cols = list(zip(*matrix))
#     for i in range(len(matrix)):
#         cols[i] = list(reversed(cols[i]))
#         matrix[i] = cols[i] 

def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
rotate(matrix)
print(matrix)