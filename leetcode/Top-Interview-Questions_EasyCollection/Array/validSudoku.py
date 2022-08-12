
def isValidSudoku(board):
    # check rows
    rows = [row for row in board]
    for row in rows:
        nums = [i for i in row if i.isdigit()]
        if len(nums) != len(set(nums)):
            return False 
    # check columns
    cols = list(zip(*board))
    for col in cols:
        nums = [i for i in col if i.isdigit()]
        if len(nums) != len(set(nums)):
            return False
    # check 3*3 sub-boxes
    subBox = []
    for i in range(3,10,3):
        for j in range(9):
            subBox += board[j][i-3:i]
            if len(subBox) == 9:
                nums = [x for x in subBox if x.isdigit()]
                if len(nums) != len(set(nums)):
                    return False
                subBox=[]
    return True



board= [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]



print(isValidSudoku(board))