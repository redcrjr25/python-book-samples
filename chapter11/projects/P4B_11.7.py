import random

def is_vowel(letter: str) -> bool:
    """Returns True if the letter is a vowel, False otherwise."""
    vowels = 'aeiouAEIOU'
    return letter.lower() in vowels

# Generate a random lowercase letter
random_letter = chr(ord('a') + random.randint(0, 25))

# Test if the letter is a vowel and print result
result = is_vowel(random_letter)
print(f" {random_letter}: {result}")