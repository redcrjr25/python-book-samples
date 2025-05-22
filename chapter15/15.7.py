# Lab 15.7 String Length Comparison - write script to test comparison function with various strings.

def compare_string_length(string1, string2):
    """
    Compares the lengths of two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
    int: -1 if string1 is shorter than string2,
         1 if string1 is longer than string2,
         0 if they are of the same length.
    """
    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    else:
        return 0

# Testing the comparison function
species_names = [
    "Python regius",  # Royal Python
    "Python molurus",  # Indian Python
    "Python sebae",  # African Rock Python
    "Python reticulatus",  # Reticulated Python
]

# Testing various combinations of species names
print("Comparison Results:")
for i in range(len(species_names)):
    for j in range(i + 1, len(species_names)):
        result = compare_string_length(species_names[i], species_names[j])
        print(f"Comparing '{species_names[i]}' with '{species_names[j]}': {result}")
