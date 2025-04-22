def product_to_n(n: int) -> int:
    """Returns the product of all integers from 1 to n (inclusive)."""
    if n <= 0:
        return 0   # Handle cases where n <= 0
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def product_of_list(numbers: list) -> int:
    """Returns the product of all numbers in the given list."""
    if not numbers:  # Handle empty list
        return 0
    product = 1
    for num in numbers:
        product *= num
    return product

# Test the function with different inputs
# Test product_to_n function
test_ns = [0, 1, 4, -1]
for n in test_ns:
    result = product_to_n(n)
    print(f"Product from 1 to {n}: {result}")

# Test product_of_list
test_lists = [[1, 2, 3], [2, 0, 4], [-1, 2, -3], []]
for lst in test_lists:
    result = product_of_list(lst)
    print(f"Product of {lst}: {result}")
# Test the function with different values of n
