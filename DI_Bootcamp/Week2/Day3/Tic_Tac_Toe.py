'''Tic Tac Toe game in Python.'''

board = [["","", ""], ["", "", ""], ["", "", ""]]

def print_board():       # A Function that Prints the Board !
    for i, row in enumerate(board):
        display = [cell if cell != "" else " " for cell in row]
        print(" | ".join(display))
        if i < 2:  
            print("--+---+--")
            

def check_winner():          # A function to test the board against the Inputs it has for a winner !
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_board_full():    # A Function to test if its a draw !
    for row in board:
        if "" in row:
            return False
    return True

def play_game():               # Getting user inputs between 0-2 to play the game | if the input is not 0-2 it will get an error !
    current_player = "X"
    while True:
        print_board()
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter row and column between 0 and 2.")
            continue
        elif board[row][col] == "":
            board[row][col] = current_player        
        else:
            print("Cell already taken, try again.")
            continue

        winner = check_winner()      # Tests the last input if it made a connection that wins it will lunch the check_winner function
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            break

        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X" 


play_game() 
