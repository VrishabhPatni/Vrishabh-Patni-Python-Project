import time
board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
winner = None
Symbol = "X"
Playing = True

# To print board


def print_board(board):
    print()
    print()
    print("\t" + board[0] + "|" + board[1] + "|" + board[2])
    print("\t---|---|---")
    print("\t" + board[3] + "|" + board[4] + "|" + board[5])
    print("\t---|---|---")
    print("\t" + board[6] + "|" + board[7] + "|" + board[8])


# To ask user for input

def user_input(board):
    global Symbol

    def valid_input(board):
        global Symbol
        print()
        num = int(input("Enter the spot from 1 to 9 to put your symbol:"))
        if 1 <= num <= 9:
            if board[num-1] == "   ":
                board[num-1] = " " + Symbol + " "
                if Symbol == "X":
                    Symbol = "O"
                else:
                    Symbol = "X"
            else:
                print()
                print("Choose a different spot:")
                valid_input(board)
        else:
            print()
            print("Enter a valid input:")
            valid_input(board)
    valid_input(board)


# To check for winner

def check_winner(board):

    if board[0] == board[1] == board[2] and board[0] != "   ":
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != "   ":
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != "   ":
        return board[6]

    elif board[0] == board[3] == board[6] and board[0] != "   ":
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != "   ":
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != "   ":
        return board[2]

    elif board[0] == board[4] == board[8] and board[0] != "   ":
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != "   ":
        return board[2]


def check_tie(board):
    global Playing
    if "   " not in board:
        print_board(board)
        print("\n\tIT IS A TIE.")
        Playing = False
    else:
        Playing = True


# Running the game

def running_game(board):
    global Playing
    global winner
    global Symbol
    while Playing == True:
        print_board(board)
        user_input(board)
        winner = check_winner(board)
        if winner != None:
            print_board(board)
            print("\n\tWINNER IS {}!!".format(winner))
            Playing = False
        else:
            check_tie(board)


print("Please input yes or no:")
time.sleep(2)
print()
inp = input("Want To play Tic Tac Toe?")
if inp.casefold() == "yes" or inp.casefold() == "no":
    if inp.casefold() == "yes":
        running_game(board)
    elif inp.casefold() == "no":
        print("Come back whenever you want to play.")
else:
    print("Please run the program again and input a valid answer.")
