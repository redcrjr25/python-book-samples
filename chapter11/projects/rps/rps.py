import random

def get_user_choice() -> str:
    """Prompts user for rock, paper, or scissors and returns r, p, or s."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        if choice.startswith('r'):
            return 'r'
        elif choice.startswith('p'):
            return 'p'
        elif choice.startswith('s'):
            return 's'
        else:
            print("Invalid input. Please enter rock, paper, or scissors")

def get_computer_choice() -> str:
    """Randomly generates r, p, or s for the computer's choice."""
    return random.choice(['r', 'p', 's'])

def determine_winner(user: str, computer: str) -> str:
    """Compares user and computer choices and returns the game result."""
    if user == computer:
        return "It's a tie!"
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return "You win!"
    else:
        return "Computer wins!"
    
def display_choices(user: str, computer: str) -> None:
    """Displays the user and computer choices."""
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    print(f"Your choice: {choice_map[user]}")
    print(f"Computer's choice: {choice_map[computer]}")

def main() -> None:
    """Main function to run the Rock-Paper-Scissors game."""
    # Get user choice
    user_choice = get_user_choice()

    # Get computer choice
    computer_choice = get_computer_choice()

    # Display choices
    display_choices(user_choice, computer_choice)

    # Determine and print winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    main()