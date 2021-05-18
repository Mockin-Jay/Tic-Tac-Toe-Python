# =============================================================================
# TWO PERSON GAME (SINGLE GAME)
# =============================================================================
# -------------------------------------------------------------
# 1. WELCOME THE USER(S)
# -------------------------------------------------------------
# welcome the users to the two player tic tac toe
print("\n\tWelcome to Two Player Tic Tac Toe!\n")
print("Player 1")
player1 = input("Enter the name: ")
print("\nPlayer 2")
player2 = input("Enter the name: ")

# -------------------------------------------------------------
# 2. LET'S CREATE A SCOREBOARD
# -------------------------------------------------------------
# let's create a list to store the scores
scores = [0, 0]
def print_scoreboard():
    print("\n\t----------------------------------------")
    print("\t               SCOREBOARD               ")
    print("\t----------------------------------------\n")
    print("\t\t    " + player1 + "\t     " + str(scores[0]))
    print("\t\t    " + player2 + "\t     " + str(scores[1]) + "\n")
    print("\t----------------------------------------\n")

# -------------------------------------------------------------
# 3. LET'S CREATE A TEMPLATE FOR USERS TO REFERENCE
# -------------------------------------------------------------
def board_template():
    print("\n")
    # first row of board
    print("\t     |     |     ")
    print("\t  1  |  2  |  3  ")
    print("\t_____|_____|_____")
    # second row of board
    print("\t     |     |     ")
    print("\t  4  |  5  |  6  ")
    print("\t_____|_____|_____")
    # third row of board
    print("\t     |     |     ")
    print("\t  7  |  8  |  9  ")
    print("\t     |     |     ")
    print("\n")

# -------------------------------------------------------------
# 4. LET'S CREATE THE BOARD DESIGN
# -------------------------------------------------------------
# let's create a list for the board values
board_values = [" ", " ", " ",
                " ", " ", " ",
                " ", " ", " "]
# new let's create the board outline
def print_board():
    print("\n")
    # first row of board
    print("\t     |     |     \t\t     |     |     ")
    print("\t  1  |  2  |  3  \t\t  " + board_values[0] + "  |  " + board_values[1] + "  |  " + board_values[2])
    print("\t_____|_____|_____\t\t_____|_____|_____")
    # second row of board
    print("\t     |     |     \t\t     |     |     ")
    print("\t  4  |  5  |  6  \t\t  " + board_values[3] + "  |  " + board_values[4] + "  |  " + board_values[5])
    print("\t_____|_____|_____\t\t_____|_____|_____")
    # third row of board
    print("\t     |     |     \t\t     |     |     ")
    print("\t  7  |  8  |  9  \t\t  " + board_values[6] + "  |  " + board_values[7] + "  |  " + board_values[8])
    print("\t     |     |     \t\t     |     |     ")
    print("\n")

# -------------------------------------------------------------
# 5. TRACK CURRENT PLAYER'S TURN
# -------------------------------------------------------------
current_player = [player1]

# -------------------------------------------------------------
# 6. FIRST (X) PLAYER TRACKER
# -------------------------------------------------------------
x_player = [player1]

# -------------------------------------------------------------
# 7. SECOND (O) PLAYER TRACKER
# -------------------------------------------------------------
o_player = [player2]

# -------------------------------------------------------------
# 8. WIN BOOLEAN
# -------------------------------------------------------------
win = [False]

# -------------------------------------------------------------
# 9. TIE BOOLEAN
# -------------------------------------------------------------
tie = [False]

# -------------------------------------------------------------
# 10. LET'S HANDLE A PLAYER'S TURN
# -------------------------------------------------------------
def player_turn():
    # ask the player for a position
    print("It is " + current_player[0] + "'s turn.")
    position = input("Choose a position from 1 to 9: ")
    if ((position == "1") or (position == "2") or (position == "3") or
        (position == "4") or (position == "5") or (position == "6") or
        (position == "7") or (position == "8") or (position == "9")):
        # convert the string into an integer
        position = int(position)
        position = position - 1
        # check if the spot is already taken
        if (board_values[position] == " "):
            # input the value into the list of the board values
            if ((current_player[0] == player1 and x_player[0] == player1) or
                (current_player[0] == player2 and x_player[0] == player2)):
                board_values[position] = "X"
            else:
                board_values[position] = "O"
            print_board()
        else:
            print("\nThis spot is already taken, please choose another spot.")
            player_turn()
    else:
        print("\nInvalid response. Please choose again.")
        player_turn()

# -------------------------------------------------------------
# 11. CHECK FOR A WINNER
# -------------------------------------------------------------
def check_win():
    # check if x won first
    if (# check if row win
        (board_values[0] == "X" and board_values[1] == "X" and board_values[2] == "X") or
        (board_values[3] == "X" and board_values[4] == "X" and board_values[5] == "X") or
        (board_values[6] == "X" and board_values[7] == "X" and board_values[8] == "X") or
        # check if column win
        (board_values[0] == "X" and board_values[3] == "X" and board_values[6] == "X") or
        (board_values[1] == "X" and board_values[4] == "X" and board_values[7] == "X") or
        (board_values[2] == "X" and board_values[5] == "X" and board_values[8] == "X") or
        # check if diagonal win
        (board_values[0] == "X" and board_values[4] == "X" and board_values[8] == "X") or
        (board_values[2] == "X" and board_values[4] == "X" and board_values[6] == "X")):
        print(x_player[0] + " wins this game!\n")
        if x_player[0] == player1:
            scores[0] = scores[0] + 1
            print_scoreboard()
            win[0] = True
        else:
            scores[1] = scores[1] + 1
            print_scoreboard()
            win[0] = True
    elif (# check if row win
        (board_values[0] == "O" and board_values[1] == "O" and board_values[2] == "O") or
        (board_values[3] == "O" and board_values[4] == "O" and board_values[5] == "O") or
        (board_values[6] == "O" and board_values[7] == "O" and board_values[8] == "O") or
        # check if column win
        (board_values[0] == "O" and board_values[3] == "O" and board_values[6] == "O") or
        (board_values[1] == "O" and board_values[4] == "O" and board_values[7] == "O") or
        (board_values[2] == "O" and board_values[5] == "O" and board_values[8] == "O") or
        # check if diagonal win
        (board_values[0] == "O" and board_values[4] == "O" and board_values[8] == "O") or
        (board_values[2] == "O" and board_values[4] == "O" and board_values[6] == "O")):
        print(o_player[0] + " wins this game!\n")
        if o_player[0] == player1:
            scores[0] = scores[0] + 1
            print_scoreboard()
            win[0] = True
        else:
            scores[1] = scores[1] + 1
            print_scoreboard()
            win[0] = True

# -------------------------------------------------------------
# 12. CHECK FOR A TIE
# -------------------------------------------------------------
def check_tie():
    filled = [True]
    for x in board_values:
        if x == " ":
            filled[0] = False
            break
    if filled[0] == True:
        print("It's a tie! No winner this game!")
        print_scoreboard()
        tie[0] = True

# -------------------------------------------------------------
# 13. NEW GAME
# -------------------------------------------------------------
new_game = [True]

# -------------------------------------------------------------
# 14. NEW GAME PLAYER TURN
# -------------------------------------------------------------
new_game_player = [player1]

# -------------------------------------------------------------
# 15. NEW GAME CHOOSING
# -------------------------------------------------------------
def new_game_setup():
    print(new_game_player[0] + ", would you like to go first (X) or second (O)?")
    print("Enter 1 for X.")
    print("Enter 2 for O.")
    print("Enter 3 to Quit.")
    play_or_quit = input("Your response: ")
    if ((play_or_quit == "1") or (play_or_quit == "2") or (play_or_quit == "3")):
        play_or_quit = int(play_or_quit)
        if play_or_quit == 1:
            current_player[0] = new_game_player[0]
            if current_player[0] == player1:
                x_player[0] = player1
                o_player[0] = player2
            else:
                x_player[0] = player2
                o_player[0] = player1
        elif play_or_quit == 2:
            if new_game_player[0] == player1:
                current_player[0] = player2
                x_player[0] = player2
                o_player[0] = player1
            else:
                current_player[0] = player1
                x_player[0] = player1
                o_player[0] = player2
        else:
            new_game[0] = False
    else:
        print("Invalid option. Please choose again.\n")
        new_game_setup()

# -------------------------------------------------------------
# 16. RESET BOARD_VALUES
# -------------------------------------------------------------
def reset_board():
    board_values[0] = " "
    board_values[1] = " "
    board_values[2] = " "
    board_values[3] = " "
    board_values[4] = " "
    board_values[5] = " "
    board_values[6] = " "
    board_values[7] = " "
    board_values[8] = " "
    win[0] = False
    tie[0] = False

# -------------------------------------------------------------
# SINGLE GAME DRIVER
# -------------------------------------------------------------
def game_driver():
    print_scoreboard()
    print("This is the cell template for your reference:")
    board_template()
    continue_game = [True]
    while new_game[0] == True:
        print("It is now " + new_game_player[0] + "'s turn.")
        new_game_setup()
        if new_game[0] == False:
            print("Final scores:")
            print_scoreboard()
            break
        else:
            print_board()
            while continue_game:
                # current player takes their turn
                player_turn()
                # check if someone won
                check_win()
                if win[0] == True:
                    break
                # check if tie
                check_tie()
                if tie[0] == True:
                    break
                # change player if no one won
                if current_player[0] == player1:
                    current_player[0] = player2
                else:
                    current_player[0] = player1
        # reset the game
        reset_board()
        # switch new_game_player
        if new_game_player[0] == player1:
            new_game_player[0] = player2
        else:
            new_game_player[0] = player1


game_driver()
