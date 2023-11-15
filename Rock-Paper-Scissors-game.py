import random

def get_user_choice():
    while True:
        user = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").capitalize()
        if user == 'Exit':
            return 'Exit'
        elif user in ["Rock", "Paper", "Scissors"]:
            return user
        else:
            print("Invalid choice. Please choose Rock, Paper, Scissors, or type 'exit' to quit.")

def play_game():
    # Generate Computer Choice
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    # Get player choice with validation
    user = get_user_choice()

    if user == 'Exit':
        return 'Exit'

    # Compare the player's choice with the computer's choice
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

    # Print result
    print('Your choice:', user)
    print('Computer choice:', computer)
    print(result)
    print()

# Play the game until the user chooses to exit
while True:
    result = play_game()
    if result == 'Exit':
        print("Exiting the game. Thanks for playing!")
        break
