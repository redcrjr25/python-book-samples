# Lab 15.10 Fibonacci Sequence - write function that generates the Fibonacci sequence for the first n numbers, e.g., using the while loop statement.

def fibonacci_iterative(n):
    """
    Generate first n numbers of the Fibonacci sequence iteratively.

    Args:
    n (int): The count of Fibonacci numbers to generate.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    fibonacci_sequence = []  # Initialize an empty list to store Fibonacci numbers
    a, b = 0, 1  # Starting values of the Fibonacci sequence

    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)  # Append the current number
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers

    return fibonacci_sequence

# Testing the iterative function
n = 10
print(
    f"First {n} numbers of the Fibonacci sequence (iterative): {fibonacci_iterative(n)}"
)

def fibonacci_recursive(n, a=0, b=1, result=None):
    """
    Generate first n numbers of the Fibonacci sequence recursively.

    Args:
    n (int): The count of Fibonacci numbers to generate.
    a (int): The first number in the Fibonacci sequence (default is 0).
    b (int): The second number in the Fibonacci sequence (default is 1).
    result (list): The list to store the Fibonacci numbers during recursion.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    if result is None:  # Initialize the result list on the first call
        result = []

    if len(result) < n:  # Check if we still need more numbers
        result.append(a)  # Append the current number
        return fibonacci_recursive(n, b, a + b, result)  # Recur with updated values

    return result

# Testing the recursive function
print(f"First {n} numbers of Fibonacci sequence (recursive): {fibonacci_recursive(n)}")
