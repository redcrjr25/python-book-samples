def string_power(base: str, exp: int) -> str:
    """Returns base repeated (len(base) ** exp) times. exp must be non-negative."""
    if exp < 0:
        return ""  # Handle negative exp as per requirement
    if not base:  # Hanndle empty string
        return ""
    repeat_count = len(base) ** exp
    return base * repeat_count

# Test the function with different strings and exponents
test_strings =  ["h", "he","hel", "hell"]
test_exponents = [0, 1, 2, 3]

for base in test_strings:
    for exp in test_exponents:
        result = string_power(base, exp)
        print(f"string_power('{base}', {exp}) = '{result}'")