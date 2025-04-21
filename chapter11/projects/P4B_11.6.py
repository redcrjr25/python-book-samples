import random

def random_arithmetic(num1: int, num2: int) -> None:
    """Performs a random arithmetic operation on two 
    numbers and prints the expression."""
    operators = ['+', '-', '*', '/', '//']
    operator = random.choice(operators)

    # Compute the result based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:  # operator == '//'
        # Handle division by zero
        if num2 == 0:
            print(f"Cannot compute {num1} // {num2} (division by zero)")
            return
        result = num1 // num2

    # Print the expression
    print(f"{num1} {operator} {num2} = {result}")

# Test the function with 5 different pairs of integers
test_pairs = [(5, 10), (20, 4), (8, 3), (15, 5), (100, 25)]

for num1, num2 in test_pairs:
    random_arithmetic(num1, num2)
# This function performs a random arithmetic operation on two numbers and prints the expression.