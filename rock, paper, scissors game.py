import random

options = ["rock", "paper", "scissors"]
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower().strip()

    print(f"Computer: {computer}")
    print(f"Player: {player}")

    if player == computer:
        print("It's a tie!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != "y":
        running = False

print("Thanks for playing!")