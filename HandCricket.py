# Common libraries and variables for whole program
import random
import time

bat_bowl = ""
toss_winner = ""


# Toss
def toss():
    global bat_bowl
    global toss_winner
    l1 = ["h", "t"]
    l2 = ["bat", "bowl"]
    result = random.choice(l1)
    time.sleep(1)
    print()
    user_input = input("Enter H for Heads and T for Tails:\t")
    time.sleep(1)
    if user_input.casefold() == result:
        print("You won the Toss.")
        toss_winner = "User"
        print()
        bat_bowl = input("Choose to Bat or Bowl:\t")
        print("You choose to {} first. ".format(bat_bowl))
    else:
        if user_input.casefold() == "h" or user_input.casefold() == "t":
            toss_winner = "Computer"
            bat_bowl = random.choice(l2)
            print("Computer won the Toss and choose to {} first. ".format(bat_bowl))
        else:
            print("Give valid input:")
            toss()


# Match Code
def user_first_batting():
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ru = 0
    user_input = 11
    computer_choice = random.choice(l1)
    print("First you are batting and computer is bowling.")
    time.sleep(1)
    print()
    while user_input != computer_choice:
        user_input = int(input("Enter a number from 0 to 10:\t"))
        if user_input not in range(0, 11):
            print("Input valid number.")
            continue
        computer_choice = random.choice(l1)
        ru = ru + user_input
        print("Your score is:" + str(ru))
        print()
        time.sleep(1)
    else:
        print("-------You are out-------")
        time.sleep(1)
    print("You scored {} runs. ".format(ru))
    time.sleep(1)
    print("Now computer will need to score {} runs to win. ".format(ru+1))
    print("------------------------------------------------------------")
    print()
    time.sleep(1)
    print("Now computer is batting and you are bowling")
    time.sleep(1)
    print()
    rc = 0
    user_input = 11
    computer_choice = random.choice(l1)
    while user_input != computer_choice:
        user_input = int(input("Enter a number from 0 to 10:\t"))
        if user_input not in range(0, 11):
            print("Input valid number.")
            continue
        computer_choice = random.choice(l1)
        rc = rc + computer_choice
        print("Computers score is:" + str(rc))
        print()
        time.sleep(1)
        if rc > ru:
            print("You have lost the match.")
            break
    else:
        print("Computer is out.")
    if ru > rc:
        print("Congratulations you have won the match.")
    elif rc == ru:
        print("Its a tie")


def user_first_bowling():
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rc = 0
    user_input = 11
    computer_choice = random.choice(l1)
    print("First you are bowling and computer is batting.")
    time.sleep(1)
    print()
    while user_input != computer_choice:
        user_input = int(input("Enter a number from 0 to 10:\t"))
        if user_input not in range(0, 11):
            print("Input valid number.")
            continue
        computer_choice = random.choice(l1)
        rc = rc + computer_choice
        print("Computers score is:" + str(rc))
        print()
        time.sleep(1)
    else:
        print("-------Computer is out-------")
        time.sleep(1)
    print("Computer scored {} runs. ".format(rc))
    time.sleep(1)
    print("Now you will need to score {} runs to win. ".format(rc+1))
    print("------------------------------------------------------------")
    print()
    time.sleep(1)
    print("Now computer is bowling and you are batting.")
    time.sleep(1)
    print()
    ru = 0
    user_input = 11
    computer_choice = random.choice(l1)
    while user_input != computer_choice:
        user_input = int(input("Enter a number from 0 to 10:\t"))
        if user_input not in range(0, 11):
            print("Input valid number.")
            continue
        computer_choice = random.choice(l1)
        ru = ru + user_input
        print("Your score is:" + str(ru))
        print()
        time.sleep(1)
        if ru > rc:
            print("Congratulations you have won the match.")
            break
    else:
        print("You are out.")
    if rc > ru:
        print("You have lost the match.")
    elif rc == ru:
        print("Its a tie")


# Match
def match():
    toss()
    print("------------------------------------------------------------")
    time.sleep(1.5)
    print()
    print("Lets start the match.")
    global bat_bowl
    global toss_winner
    if toss_winner == "User" and bat_bowl.casefold() == "bat":
        user_first_batting()
    elif toss_winner == "User" and bat_bowl.casefold() == "bowl":
        user_first_bowling()
    elif toss_winner == "Computer" and bat_bowl == "bat":
        user_first_bowling()
    else:
        user_first_batting()


while True:
    print("Enter yes or no")
    inp = input("Want to play Hand Cricket?\t")
    time.sleep(1)
    if inp.casefold() == "yes":
        print()
        print("First lets have a Toss.")
        match()
        break
    elif inp.casefold() == "no":
        print()
        print("Coward comeback whenever you feel that you can defeat me.")
        break
    else:
        print("Enter a valid input.")
