
#Number guessing game

import random

def numberGuessingGame():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100 randomly.")

    ComputerChoice = random.randint(1, 100)
    attempts = 0

    while True:
        try:
          userGuess = int(input("Please enter your guess: "))

          if userGuess < 1 or userGuess > 100:
            print("Please choose a number between 1 and 100.")
            continue

        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue
    
        attempts += 1

        if userGuess < ComputerChoice:
            print("Too low! Try again.")

        elif userGuess > ComputerChoice:
            print("Too high! Try again.")

        else:
            print(f"Congratulations! You've guessed the number {ComputerChoice} in {attempts} attempts.")
            break

if __name__ == "__main__":
  numberGuessingGame()


