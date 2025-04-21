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
user_input = input("Enter a suit (Spade, Heart, Diamond, or Clubs): ")

# Get the corresponding letter
letter = get_suit_letter(user_input)

# Print the user input and selected letter
print(f"Input: {user_input}")
print(f"Selected letter: {letter}")