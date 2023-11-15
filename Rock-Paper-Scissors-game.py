#Get player choice
def get_user_choice():
    while True:
        user = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user in ["Rock", "Paper", "Scissors"]:
            return user
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Get player choice with validation
user = get_user_choice()

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

#print result
print(f'Your choice: {user}')
print(f'Computer choice: {computer}')
print(result)