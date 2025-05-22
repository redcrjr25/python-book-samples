# Length Function - Calculate the length of list withough len function

def iterative_length(int_list):
    """Calculate the length of the list iteratively."""
    count = 0
    for _ in int_list:
        count += 1
    return count

def recursive_length(int_list):
    """Calculate the length of the list recursively using match-case."""
    match int_list:
        case []:  # Base case: if the list is empty
            return 0
        case [_] | [_, *_]:  # Case when there is at least one element
            return 1 + recursive_length(int_list[1:])  # Count this element and continue

def test_length_functions():
    """Test the implementations with various sample lists."""
    sample_lists = [
        [1, 2, 3],
        [10],
        [],
        [5, 6, 7, 8, 9],
        [-1, -2, -3],
        [0],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    for sample in sample_lists:
        print(f"Testing list: {sample}")
        print(f"Iterative length: {iterative_length(sample)}")
        print(f"Recursive length: {recursive_length(sample)}")
        print("---")

if __name__ == "__main__":
    test_length_functions()
