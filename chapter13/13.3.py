def filtered_sum(n, /, *, excluded=None) -> int:
    """Sums numbers from 0 to n, excluding numbers in the excluded list."""
    if n < 0:
        return 0  # Handle negative n as per non-negative requirement
    total = 0
    # If excluded is not provided, set it to an empty list
    if excluded is None:
        excluded = []
    for i in range(n + 1):  # Sum from 0 to n inclusive
        if i not in excluded:  # Skip numbers in the excluded list
            total += i
    return total

# Test the function with different inputs
test_cases = [
    (5, [3, 4, 10]),  # Should sum 0 + 1 + 2 + 5 = 8
    (5, []),          # Should sum 0 + 1 + 2 + 3 + 4 + 5 = 15
    (3, [1]),         # Should sum 0 + 2 + 3 = 5
    (0, []),          # Should sum 0 = 0
    (5, None),        # Should sum 0 + 1 + 2 + 3 + 4 + 5 = 15
]

for n, excluded in test_cases:
    result = filtered_sum(n, excluded=excluded)
    print(f"Sum from 0 to {n}, excluding {excluded}: {result}")