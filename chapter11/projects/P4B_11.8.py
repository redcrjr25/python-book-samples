import random

def check_bools() -> None:
    """Generates three random booleans and prints if all are the same or counts True/False."""
    # Generate three random booleans
    bools = [random.choice([True, False]) for _ in range(3)]

    # Count True values
    true_count = bools.count(True)
    false_count = 3 - true_count   # Since there are only 3 values

    # Check if all booleans are the same
    if true_count == 3:
        print("All are True")
    elif false_count == 3:
        print("All are False")
    else:
        print(f"{true_count} true and {false_count} false")
              
# Call the function 10 times
for _ in range(10):
    check_bools()
              