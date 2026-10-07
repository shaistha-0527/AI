board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


def play_game():
    player = "X"

    for turn in range(9): 
        display_board()

        print("Player", player, "turn")

        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position!")
            continue

        if board[position] != " ":
            print("Position already occupied!")
            continue

        board[position] = player

        if check_winner(player):
            display_board()
            print("Player", player, "wins!")
            return

        if turn == 8:
            display_board()
            print("It's a draw!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"


play_game()