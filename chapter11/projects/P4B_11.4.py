def to_uppercase(text: str) -> str:
    """Converts the input string to uppercase."""
    return text.upper()

# Get user input
user_input = input("Enter a string: ")

# Convert to uppercase and print
result = to_uppercase(user_input)
print(f"The uppercase version is: {result}")