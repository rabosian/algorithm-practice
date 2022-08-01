def gridChallenge(grid):
    newList = []
    rows = [row for row in grid]
    for row in rows:
        newList.append(sorted(row))
    cols = list(zip(*newList))
    for col in cols:
        if sorted(col) != list(col):
            return 'NO'
    return 'YES'


grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(grid))