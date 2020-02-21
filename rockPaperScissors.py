from random import randint

options = ["rock", "paper", "scissors"]

computer = options[randint(0,2)]

player = False

while player == False:
    player = input("Rock? Paper? Scissors?")
    if player == computer:
        print("Player and computer tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else: print ("You win!", player, "demolishes", computer)
    elif player == "paper":
        if computer == "rock":
            print ("You win!", player, "covers", computer)
        else: print ("You lose!", computer, "cuts", player)
    elif player == "scissors":
        if computer == "paper":
            print("You win!", player, "cuts", computer)
        else: print("You lose!", computer, "demolishes", player)

    else:
        print("Not a valid input.")

    player = False
    computer = options[randint(0, 2)]