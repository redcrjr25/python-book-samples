import random

def get_suit_letter(suit: str) -> str:
    """Returns the corresponding letter based on the first letter of the suit."""
    suit = suit.lower().strip()
    if suit.startswith('s'):
        return 's'
    elif suit.startswith('h'):
        return 'h'
    elif suit.startswith('d'):
        return 'd'
    elif suit.startswith('c'):
        return 'c'
    else:
        return 'unknown'
# Get user input

def pick_random_suit() -> str:
    """Randomly picks one of the four suit letters: s, h, d, or c."""
    suits = ['s', 'h', 'd', 'c']
    return random.choice(suits)

# Get user input and convert to suit letter
user_input = input("Enter a suit (Spade, Heart, Diamond, or Clubs): ")
user_suit = get_suit_letter(user_input)

# Generate a random suit letter
random_suit = pick_random_suit()

# Compare the suits and print the result
if user_suit == random_suit:
    print("The same suit. You win!")
else:
    print("Different suits. Try again.")
