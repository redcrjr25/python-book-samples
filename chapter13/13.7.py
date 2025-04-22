from typing import List

def reverse_in_place_for(arr: List[int]) -> None:
    """Reverses the given list in-place using a for loop."""
    n = len(arr)
    # Iterate up to half the list length to swap elements
    for i in range(n // 2):
        # Swap elements at i and (n-1-i)
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

def reverse_in_place_while(arr: List[int]) -> None:
    """Reverses the given list in-place using a while loop."""
    left = 0
    right = len(arr) - 1
    # Swap elements from both ends until pointers meet
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def reverse_new_list(arr: List[int]) -> List[int]:
    """Returns a new list with elements in reverse order."""
    # Create a new list with the same elements
    result = arr.copy()
    # Use a for loop to reverse the new list in-place
    n = len(result)
    for i in range(n // 2):
        result[i], result[n - 1 - i] = result[n - 1 - i], result[i]
    return result

# Test the functions
# Test reverse_in_place (both versions)
test_lists = [[1, 2, 3, 4], [5, 6, 7], [], [1], [1, 2]]
for arr in test_lists:
    # Test with for loop
    arr_copy = arr.copy()
    reverse_in_place_for(arr_copy)
    print(f"reverse_in_place_for({arr}) -> {arr_copy}")
    
    # Test with while loop
    arr_copy = arr.copy()
    reverse_in_place_while(arr_copy)
    print(f"reverse_in_place_while({arr}) -> {arr_copy}")

# Test reverse_new_list
for arr in test_lists:
    result = reverse_new_list(arr)
    print(f"reverse_new_list({arr}) -> {result}, original: {arr}")