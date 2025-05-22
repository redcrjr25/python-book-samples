# String Concat Function - writes function takes list of strings and returns string which is concatenation of all items in the list sep by commas.

def concatenate_strings_iteratively(str_list):
    """
    Concatenates a list of strings into a single string, separated by commas, using iteration.

    Args:
    str_list (list): A list of strings to concatenate.

    Returns:
    str: A single concatenated string.
    """
    result = ""
    for index, item in enumerate(str_list):
        result += item
        if index < len(str_list) - 1:  # Avoid adding a comma after the last item
            result += ", "
    return result

def concatenate_strings_recursively(str_list):
    """
    Concatenates a list of string into a single string, separated by commas, using recursion.

    Args:
    str_list (list): A list of strings to concatenate.

    Returns:
    str: A single concatenated string.
    """
    match str_list:
        case []:
            return ""
        case [first, *rest]:  # Unpacking the first element from the rest
            if rest:  # If there are remaining elements
                return first + ", " + concatenate_strings_iteratively(rest)
            else:
                return first  # If it's the last item

# Testing the two implementations
sample_lists = [
    ["Pythons eat mice", "lizards", "birds", "pigs", "monkeys"],
    ["apples", "bananas", "cherries"],
    ["one", "two", "three", "four", "five"],
    [],
]

for sample in sample_lists:
    iter_result = concatenate_strings_iteratively(sample)
    rec_result = concatenate_strings_recursively(sample)

    print(f"Sample: {sample}")
    print(f"Iterative Result: '{iter_result}'")
    print(f"Recursive Result: '{rec_result}'")
    print()  # Adding a newline for better format
