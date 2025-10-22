def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([" ".join("Q" if c == 1 else "." for c in r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0


def print_solutions(solutions):
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()


def main():
    n = int(input("Enter the number of queens: "))
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    if solutions:
        print_solutions(solutions)
        print(f"Total solutions: {len(solutions)}")
    else:
        print("No solutions found.")


if __name__ == "__main__":
    main()
