import random

# Constants
R, P, S = "r", "p", "s"
WIN, LOSS, TIE = "w", "l", "t"

def user_hand() -> str:
    """Reads user input and converts it to a constant (r, p, or s)."""
    while True:
        choice = input("Rock (r), Paper (p), or Scissors (s)? ").strip()
        if choice.lower() in [R, P, S]:
            return choice.lower()
        print("Invalid input. Please enter r, p, or s.")

def computer_hand() -> str:
    """Randomly generates a computer hand (r, p, or s)."""
    return random.choice([R, P, S])

def determine_win(user: str, computer: str) -> str:
    """Compares two hands and decides which hand wins."""
    if user == computer:
        return TIE
    if (user == R and computer == S) or (user == P and computer == R) or (user == S and computer == P):
        return WIN
    return LOSS

def f1() -> str:
    """Plays one round: reads user hand, generates computer hand, determines winner."""
    user = user_hand()
    computer = computer_hand()
    result = determine_win(user, computer)
    return result