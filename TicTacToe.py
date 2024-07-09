from IPython.display import clear_output

# This function displays the board to the user
def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' '+ board[7]+' '+'|'+ ' '+ board[8]+' '+'|'+ ' '+ board[9]+' ')
    print('---|---|---')
    print(' '+ board[4]+' '+'|'+ ' '+ board[5]+' '+'|'+ ' '+ board[6]+' ')
    print('---|---|---')
    print(' '+ board[1]+' '+'|'+ ' '+ board[2]+' '+'|'+ ' '+ board[3]+' ')
    print('   |   |   ')

# Function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    
    marker = 'Wrong'

    while marker not in ['x','X','o','O']:

        marker = input("Player 1: Select your symbol (X or O): ")

        if marker not in ['x','X','o','O']:
            print("Sorry, the caracter you enter is not a correct symbol for this game. Try again!")
    
    return marker

# This function takes the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

# This function checks all positions where the marker is the same and the player can win the game.
def win_check(board, mark):

    # First row
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True

    # Second row
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True

    # Third row
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True

    # First column
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True

    # Second column
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True

    # Third column
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True

    # Diagonal 1
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    # Diagonal 2
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False
    

import random
# Function to randomly select the player who starts the game.
def choose_first():
    a = random.randint(1,2)
    if a == 1:
        return 'X'
    else:
        return 'O'

# Function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    if board[position] == '.':
        return True
    else:
        return False

# Function that checks if the board is full and returns a boolean value.
def full_board_check(board):
    # If there are no empty positions in the list, returns true
    if '.' not in board:
        return True
    else:
        return False

# Function that asks for a player's next position (as a number 1-9)
def player_choice(board):
    choice = 'Wrong'

    while choice not in ['1','2','3','4','5','6','7','8','9']:

        choice = input("Pick a position (1-9): ")

        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry, invalid value!")
        elif space_check(board,int(choice)) == False:
            print("Sorry, an element already exists in this position")
            choice = 'Wrong'
    return int(choice)

# Function that asks the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    
    ask = 'wrong'

    while ask not in ['Y','y','N','n']:

        ask = input("Do you want to play again? (Y or N): ")

        if ask not in ['Y','y','N','n']:
            print("Invalid character")
    
    if ask in ['Y','y']:
        return True
    else: 
        return False
    

# Game Logic

print('Welcome to Tic Tac Toe!')
print("The board consists of positions ranging from the lowest to the highest row in order from 1 to 9.")
print("Enjoy the game!")

gameon = True

while gameon:
    board = ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    display_board(board)

    player1 = ''
    while player1 not in ['X', 'O', 'x', 'o']:
        # User input for player 1
        player1 = player_input()
        if player1 in ['X', 'x']:
            player1 = 'X'
            player2 = 'O'
            print(f"The player 1 is playing with {player1} while player 2 is playing with {player2}")
        elif player1 in ['O', 'o']:
            player1 = 'O'
            player2 = 'X'
            print(f"The player 1 is playing with {player1} while player 2 is playing with {player2}")
        else:
            print("Sorry that is not a correct symbol for this game!")

    # A random player turn is chosen
    current_player = choose_first()
    print(f'{current_player} will go first.')

    match_tic = True
    while match_tic:
        print(f"Turn of {current_player}")
        position = player_choice(board)
        place_marker(board, current_player, position)
        display_board(board)

        if win_check(board, current_player):
            print(f"THE PLAYER {current_player} HAS WON THE GAME!!!!")
            match_tic = False
        elif full_board_check(board):
            print("The board is full! It's a tie!")
            match_tic = False
        else:
            # If the current player is player 2, change to player 1.
            if current_player == player2:
                current_player = player1
            # Otherwise, switch to player 2
            else:
                current_player = player2

    if not replay():
        gameon = False