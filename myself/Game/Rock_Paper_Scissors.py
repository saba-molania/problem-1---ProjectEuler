import random

print("Welcome to Rock, Paper, Scissors!\n")

player_wins = 0
computer_wins = 0

while True:
    player = input("Enter a choice (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer}.")

    if player == computer:
        print(f"Both players selected {player}. It is a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors. you win!")
            player_wins += 1
        else:
            print("paper covers rock. you lose.")
            computer_wins +=1
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock. You win!")
            player_wins+=1
        else:
            print("Scissors cuts paper. You lose.")
            computer_wins+=1
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper. You win!")
            player_wins+=1
        else:
            print("Rock smashes scissors. You lose.")
            computer_wins += 1

    print("You have "+str(player_wins)+" wins")
    print("The computer has "+str(computer_wins)+" wins")

    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break