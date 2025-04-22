# Rock, Paper, Scissors Game

import random

def get_user_choice() -> str:
    """Prompts user for rock, paper, or scissors and returns r, p, or s."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors, or 'quit' to exit): ").lower().strip()
        if choice == 'quit':
            return 'quit'
        if choice.startswith('r'):
            return 'r'
        elif choice.startswith('p'):
            return 'p'
        elif choice.startswith('s'):
            return 's'
        else:
            print("Invalid input. Please enter rock, paper, scissors, or 'quit'.")

def get_computer_choice() -> str:
    """Randomly generates r, p, or s for the computer's choice."""
    return random.choice(['r', 'p', 's'])

def determine_winner(user: str, computer: str) -> str:
    """Compares user and computer choices and returns the game result."""
    if user == computer:
        return "tie"
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return "user"
    else:
        return "computer"

def display_choices(user: str, computer: str) -> None:
    """Displays the user and computer choices."""
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    print(f"Your choice: {choice_map[user]}")
    print(f"Computer's choice: {choice_map[computer]}")

def main() -> None:
    """Main function to run the rock, paper, scissors game with multiple rounds."""
    user_score = 0
    computer_score = 0
    tie_count = 0
    
    while True:
        # Get user choice
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break
        
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Display choices
        display_choices(user_choice, computer_choice)
        
        # Determine and print winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
            tie_count += 1
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Display current score
        print(f"Score - You: {user_score}, Computer: {computer_score}, Ties: {tie_count}\n")
    
    # Display final score
    print("\nFinal Score:")
    print(f"You: {user_score}, Computer: {computer_score}, Ties: {tie_count}")
    if user_score > computer_score:
        print("You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner!")
    else:
        print("The game ends in a tie!")

# Run the game
if __name__ == "__main__":
    main()