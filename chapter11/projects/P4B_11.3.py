def is_positive(number: int) -> bool:
    """Returns True if the number is positive, otherwise False."""
    return number > 0

# Test the function
test_numbers = [-10, 0, 5, 20]

for num in test_numbers:
    if is_positive(num):
        print(f"{num} is positive.")
    else:
        print(f"{num} is not positive.")
# The function is_positive checks if a number is positive.
# It returns True if the number is greater than 0, otherwise it returns False.
# The test cases include negative, zero, and positive numbers.
# The output will indicate whether each number is positive or not.
# The function is_positive checks if a number is positive.
# It returns True if the number is greater than 0, otherwise it returns False. 