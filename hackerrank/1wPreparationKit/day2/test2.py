# Flipping the Matrix

def flippingMatrix(matrix):
    n = len(matrix) // 2
    rows = matrix[:2]
    target = [row[:2] for row in rows]
    # sum(row, []) => convert 2d to 1d array
    maxSum = sum(sum(target, []))

    # row loop
    for i in range(len(target)):



    # cols = list(zip(*matrix))



matrix = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]

print(flippingMatrix(matrix))
