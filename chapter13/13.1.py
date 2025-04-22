# Function with integer argument
# We will write a function with a conditional to handle positive and negative numbers.
# Using a loop to calculate the sum.
# Test the function with a variety of inputs.

def sum_to_n(n: int) -> int:
    """Returns the sum from 0 to n if n >= 0, or from n to 0 if n < 0."""
    total = 0
    if n >= 0:
        # Sum from 0 to n (inclusive)
        for i in range(n + 1): # range(n + 1) goes from 0 to n
            total += i
    else:
        # Sum from n to 0 (inclusive)
        for i in range(n, 1):  # range(n, 1) goes from n to 0
            total += i
    return total

# Test the function with different values of n
test_values = [0, 5, 10, -5, -10]
for n in test_values:
    result = sum_to_n(n)
    print(f"Sum from {min(0, n)} to {max(0, n)} for n = {n}: {result}")