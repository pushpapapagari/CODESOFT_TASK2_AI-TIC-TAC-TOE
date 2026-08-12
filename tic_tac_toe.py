def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def check_draw(board):
    return " " not in board


def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -100

        for move in get_available_moves(board):
            board[move] = "O"

            score = minimax(board, False)

            board[move] = " "

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for move in get_available_moves(board):
            board[move] = "X"

            score = minimax(board, True)

            board[move] = " "

            best_score = min(best_score, score)

        return best_score


def find_best_move(board):
    best_score = -100
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"

        score = minimax(board, False)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# -------------------------------
# MAIN GAME
# -------------------------------

board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]

print("Welcome to Tic-Tac-Toe!")
print("You are X. Computer is O.")
print("Choose a position from 1 to 9.")

while True:

    print_board(board)

    # Player's move
    try:
        move = int(input("Enter your move (1-9): "))
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if move < 1 or move > 9:
        print("Invalid move! Please choose a number from 1 to 9.")
        continue

    if board[move - 1] != " ":
        print("That position is already taken. Try again.")
        continue

    board[move - 1] = "X"

    winner = check_winner(board)

    if winner == "X":
        print_board(board)
        print("🎉 Congratulations! You won!")
        break

    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    print("Computer is thinking...")

    computer_move = find_best_move(board)

    board[computer_move] = "O"

    winner = check_winner(board)

    if winner == "O":
        print_board(board)
        print("🤖 Computer wins! Better luck next time!")
        break

    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break