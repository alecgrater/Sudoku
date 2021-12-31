board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

# locate first empty square, denoted with a zero.
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)


def check_valid(board, num, pos):
    # checking row
    temp_list_row = [i for i in board[pos[0]]]
    if num in temp_list_row:
        return False

    # checking column
    temp_list_column = [i[pos[1]] for i in board]
    if num in temp_list_column:
        return False

    # checking box
    temp_list_box = []
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for k in board[box_row * 3 : box_row * 3 + 3]:
        for l in k[box_col * 3 : box_col * 3 + 3]:
            temp_list_box.append(l)
    if num in temp_list_box:
        return False

    return True


# backtracing algorithm via recursive function. try 1-9 on each square
# if board is unsolvable, retry previous square
def solve(board):
    empty_square = find_empty(board)
    if empty_square:
        row, col = empty_square
    else:
        return True
    for i in range(1, 10):
        if check_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
    board[row][col] = 0
    return False


# prints board to console in readable format
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(board1)
solve(board1)
print("___________________")
print("___________________")
print("___________________")
print_board(board1)
