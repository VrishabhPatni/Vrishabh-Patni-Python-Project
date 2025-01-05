import random
import time

num = 0


def rolling_dice():
    global num
    num = random.randint(1, 6)


print()
print("Let's play a 2 player gambling game.")
print()

score_player1 = 0
score_player2 = 0

time.sleep(1)
print("Rules of the game:")
print("=>Choose to role the dice or not.")
print("=>Each number occuring on the dice will add up to your score.")
print("=>Except for 1.")
print("=>If 1 occurs then your score will reset to zero and next players turn comes up.")
print("=>The player to score 30 wins the game.")
time.sleep(3)

while score_player1 < 30 and score_player2 < 30:
    print()
    time.sleep(1)
    print("Chance of player 1:")
    print("Always enter 'Y' for Yes and 'N' for No.")
    while True:
        print()
        time.sleep(1)
        ch = input("Want to role the dice:")
        if ch.casefold() == "y":
            rolling_dice()
            print("Number on the dice is {0}.".format(num))
            if num == 1:
                score_player1 = 0
                print("You are down to 0.")
                break
            else:
                score_player1 += num
                if score_player1 >= 30:
                    break
        elif ch.casefold() == "n":
            print("Your final score is {0}".format(score_player1))
            break
        else:
            print()
            print("Enter a valid input:")
    if score_player1 >= 30:
        print("Player 1 has won by scoring {0}.".format(score_player1))
        break

    print()
    time.sleep(1)
    print("Chance of player 2:")
    print("Always enter 'Y' for Yes and 'N' for No.")
    while True:
        print()
        time.sleep(1)
        ch = input("Want to role the dice:")
        if ch.casefold() == "y":
            rolling_dice()
            print("Number on the dice is {0}.".format(num))
            if num == 1:
                score_player2 = 0
                print("You are down to 0.")
                break
            else:
                score_player2 += num
                if score_player2 >= 30:
                    break
        elif ch.casefold() == "n":
            print("Your final score is {0}".format(score_player1))
            break
        else:
            print()
            print("Enter a valid input:")
    if score_player2 >= 30:
        print("Player 2 has won by scoring {0}.".format(score_player2))
print("Thank you for gambling.")
