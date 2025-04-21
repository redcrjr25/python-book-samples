import random

def pick_random_suit() -> str:
    """Randomly picks one of the four suit letters: s, h, d, or c."""
    suits = ['s', 'h', 'd', 'c']
    return random.choice(suits)

# Pick and print a random suit letter
suit = pick_random_suit()
print(f"Random suit letter: {suit}")