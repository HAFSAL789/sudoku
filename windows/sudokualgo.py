import copy

# sudoku board

board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9],
         ]

length = len(board)

# To check a number is suitable in current position(row,column)
# number --- 0 to 9


def checker(row, column, number):
    # To check the number is present twice in any row
    if number not in board[row]:
        # to check number is present twice in any 3*3 square
        # rowlimit,columnlimit -- to determine the number is in which square
        rowlimit = 8
        if row <= 2:
            rowlimit = 2
        elif row <= 5:
            rowlimit = 5
        columnlimit = 8
        if column <= 2:
            columnlimit = 2
        elif column <= 5:
            columnlimit = 5
        # to check the number is present twice the selected square
        for squarechecker in range(rowlimit-2, rowlimit+1):
            if number in board[squarechecker][columnlimit-2:columnlimit+1]:
                return
        # To check the number is present twice in any column
        for coulmnchecker in range(length):
            if number == board[coulmnchecker][column]:
                return
        return True

# to select numbers from 0 to 9


def selecting(row,column):
    for number in range(1,length+1):
        # to check if selected number is possible to place in the position
        if checker(row, column, number):
            board[row][column] = number
            start()
    # backtracking
    board[row][column] = 0


copyboard = board


# check the board is solved after user guessing the last zero column
def check_user(board):
    set1 = set()
    for row in range(9):
        if len(set(board[row])) != 9:
            return "False"
        for coulmnchecker in range(9):
            set1.add(board[row][coulmnchecker])
        if len(set1) != 9:
            return "False"
    for row in range(0,9,3):
        for loop in range(0,9,3):
            set2 = set(board[row][loop:loop+3]).union(set(board[row+1][loop:loop+3])).union(set(board[row+2][loop:loop + 3]))
            if len(set2) !=9:
                return "False"
    return "True"

# main function


def start():
    global copyboard
    for row in range(length):
        for column in range(length):
            if board[row][column] == 0:
                selecting(row,column)
                return
    copyboard = copy.deepcopy(board)
    return
