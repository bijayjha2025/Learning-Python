#Guess the word game

import random

def guessTheWord():
    words = ['python', 'programming', 'c', 'maths', 'loop', 'function', 'boolean', 'nepal', 'technology', 'brainrot']
    secretWord = random.choice(words)

    guessedLetters = []
    attempts = 6

    print("Welcome to the Guess The Word Game!")
    print("I have chosen a secret word. You have 6 attempts to guess it letter by letter.")

    while attempts > 0:
        displayWord = ''.join([letter if letter in guessedLetters else '_' for letter in secretWord])
        print(f"Word: {displayWord}")
        print(f"Attempts remaining: {attempts}")

        userGuess = input("Please enter a letter: ").lower()

        if len(userGuess) != 1 or not userGuess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if userGuess in guessedLetters:
            print("You have already guessed that letter. Try again.")
            continue

        guessedLetters.append(userGuess)

        if userGuess not in secretWord:
            attempts -= 1
            print(f"Wrong guess! The letter '{userGuess}' is not in the word.")

        if all(letter in guessedLetters for letter in secretWord):
            print(f"Congratulations! You've guessed the word '{secretWord}' correctly!")
            break

    else:
        print(f"Sorry, you've run out of attempts. The secret word was '{secretWord}'.")

if __name__ == "__main__":
    guessTheWord()