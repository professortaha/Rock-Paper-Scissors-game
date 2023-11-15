#Get player choice
user = input("Choose Rock, Paper, or Scissors: ")

#Generate Computer Choice
import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

#Compare the player's choice with the computer's choice
if user == computer:
    result = "It's a tie!"
elif (
    (user == "Rock" and computer == "Scissors") or
    (user == "Paper" and computer == "Rock") or
    (user == "Scissors" and computer == "Paper")
):
    result = "You win!"
else:
    result = "You lose!"
