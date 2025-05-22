# Sum Function - write function that takes a list of int and returns sum of all items without using sum function

def sum_iteratively(int_list):
    total = 0  # Initialize the sum to zero
    for num in int_list:
        total += num  # Add each number to the total
    return total  # Return the accumulated sum

def sum_recursively(int_list):
    # Base condition: if the list is empty, the sum is 0
    if not int_list:
        return 0
    else:
        # Recursive case: sum the first element and the sum of the rest of the list
        first_element = int_list[0]
        remaining_list = int_list[1:]
        return first_element + sum_recursively(remaining_list)

def test_sum_functions():
    test_cases = [
        [1, 2, 3, 4, 5],
        [-1, -2, -3],
        [0, 0, 0],
        [10, 20, 30],
        [],
        [-5, 5, 2, 3, -3],
    ]

    for i, test_case in enumerate(test_cases, start=1):
        iter_sum = sum_iteratively(test_case)
        rec_sum = sum_recursively(test_case)
        print(
            f"Test Case {i}: {test_case} -> Iterative Sum: {iter_sum}, Recursive Sum: {rec_sum}"
        )

# Run the tests
test_sum_functions()
