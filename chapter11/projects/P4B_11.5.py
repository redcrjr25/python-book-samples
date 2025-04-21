import random

def pick_random_letters() -> tuple[str, str]:
    """Picks two different random lowercase letters."""
    # Generate two different random numbers between 0 and 15 (for letters a-z)
    index1 = random.randint(0, 25)
    index2 = random.randint(0, 25)
    while index1 == index2:   # Ensure the letters are different
        index2 = random.randint(0, 25)
    
    # Convert indices to letters (a=0, b=1, ..., z=25)
    letter1 = chr(ord('a') + index1)
    letter2 = chr(ord('a') + index2)

    return letter1, letter2

# Test the function
letter1, letter2 = pick_random_letters()
print(f"The two random letters are: {letter1} and {letter2}")
# The function pick_random_letters generates two different random lowercase letters.