#Snake Water Gun Game

# #Logic:
# Snake drinks Water → Snake wins
# Water douses Gun → Water wins
# Gun kills Snake → Gun wins
# Same choice → Draw

import random

def snakeWaterGunGame():
    choices = ['snake', 'water', 'gun']
    computerChoice = random.choice(choices)

    print("Welcome to the Snake Water Gun Game!")
    print("Choices: snake, water, gun")

    userChoice = input("Please enter your choice: ").lower()

    if userChoice not in choices:
        print("Invalid choice! Please choose either 'snake', 'water', or 'gun'.")
        return
    
    print(f"Computer chose: {computerChoice}")

    if userChoice == computerChoice:
        print("It's a draw!")

    elif (userChoice == 'snake' and computerChoice == 'water') or (userChoice == 'water' and computerChoice == 'gun') or (userChoice == 'gun' and computerChoice == 'snake'):
        print("You win!")

    else:
        print("Computer wins!")

if __name__ == "__main__":
    snakeWaterGunGame()