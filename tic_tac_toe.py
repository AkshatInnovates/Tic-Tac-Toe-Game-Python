# printing the game board
# Function to initialize the board
def initialize_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True

    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to get player's move
def get_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if not (0 <= row <= 2) or not (0 <= col <= 2):
                raise ValueError("Invalid input. Row and column must be between 0 and 2.")
            return (row, col)
        except ValueError as e:
            print(e)

# Main function to run the game
def play_game():
    board = initialize_board()
    current_player = 'X'

    while True:
        # Print the current board
        print_board(board)

        # Get the player's move
        print(f"Player {current_player}'s turn.")
        row, col = get_move()

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check if the game is a draw
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = 'O'
        else:
            print("Invalid move. The cell is already occupied. Try again.")

if __name__ == "__main__":
    play_game()

#