from sudoku import Sudoku

# locate first empty square, denoted with a zero.
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)


def check_valid(board, num, pos):
    # check row
    temp_list_row = [i for i in board[pos[0]]]
    if num in temp_list_row:
        return False

    # check column
    temp_list_column = [i[pos[1]] for i in board]
    if num in temp_list_column:
        return False

    # check box.
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
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def print_title(is_solved):
    if is_solved == False:
        title = "       UNSOLVED:       "
    else:
        title = "        SOLVED:        "
    print("\n")
    print(title)
    print("_______________________")
    print("\n")


def main():
    # generate new puzzle via sudoku package
    # note this package can also solve puzzles, this project is purely for fun
    puzzle = Sudoku(3)
    board = puzzle.board

    # module denotes empties with None instead of 0, so...
    for lst in board:
        for index, item in enumerate(lst):
            if item == None:
                lst[index] = 0

    print_title(is_solved=False)
    print_board(board)

    solve(board)

    print_title(is_solved=True)
    print_board(board)
    print("\n")


if __name__ == "__main__":
    main()
