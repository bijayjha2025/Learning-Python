
import random

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
if user not in choices:
    print("Invalid choice")
    exit()

computer = random.choice(choices)
print(f"Computer chose: {computer}")

if user == computer:
    print("Result: Draw")
elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("Result: You win")
else:
    print("Result: You lose")
