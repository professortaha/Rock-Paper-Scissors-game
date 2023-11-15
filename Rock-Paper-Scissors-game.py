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

def play_game(stats):
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
        stats['wins'] += 1
    else:
        result = "You lose!"
        stats['losses'] += 1

    stats['rounds'] += 1

    # Print result and stats
    print('Your choice:', user)
    print('Computer choice:', computer)
    print(result)
    print(f"Rounds: {stats['rounds']}, You win: {stats['wins']}, You lose: {stats['losses']}")
    print()

# Initialize game stats
game_stats = {'rounds': 0, 'wins': 0, 'losses': 0}

# Play the game until the user chooses to exit
while True:
    result = play_game(game_stats)
    if result == 'Exit':
        print("Game statistics:")
        print(f"Total Rounds: {game_stats['rounds']}")
        print(f"You Win: {game_stats['wins']}")
        print(f"You Lose: {game_stats['losses']}")
        print("Exiting the game. Thanks for playing!")
        break
