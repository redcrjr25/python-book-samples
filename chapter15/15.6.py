# Product Function - writing a function that reurns product for list of ints.

def product_iteratively(int_list):
    product = 1  # Intialize the product to 1 (multiplicative identity)
    for num in int_list:
        product *= num  # Multiply each number to the product
    return product  # Return the accumulated product

def product_recursively(int_list):
    # Base condition: If the list is empty, the product is 1
    if not int_list:
        return 1
    else:
        # Recursive case: multiply the first element with the product of the rest or the list
        first_element = int_list[0]
        remaining_list = int_list[1:]
        return first_element * product_recursively(remaining_list)

def test_product_functions():
    test_cases = [
        [1, 2, 3, 4],
        [-1, -2, -3],
        [0, 1, 2, 3],
        [10, -1],
        [],
        [-5, 5, 2, 3, -3],
    ]

    for i, test_case in enumerate(test_cases, start=1):
        iter_product = product_iteratively(test_case)
        rec_product = product_recursively(test_case)
        print(
            f"Test Case {i}: {test_case} -> Iterative Product: {iter_product}, Recursive Product: {rec_product}"
        )

# Run the tests
test_product_functions()
