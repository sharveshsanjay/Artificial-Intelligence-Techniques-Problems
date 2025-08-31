# N-Queens problem adapted as Guards placement
N = 4  # Size of the grid

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join('G' if col else '.' for col in row))
    print()

# Check if it's safe to place a guard at board[row][col]
def is_safe(board, row, col):
    # Check vertical up
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function
def solve_n_queens(board, row):
    if row == N:
        print_board(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = 0  # Backtrack
    return res

# Initialize the board
board = [[0 for _ in range(N)] for _ in range(N)]
print("Valid configurations for placing 4 guards:\n")
solve_n_queens(board, 0)
