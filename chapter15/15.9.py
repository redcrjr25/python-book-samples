# Multiplicaton Table - create table between integers 2 and 12.

def print_multiplication_table():
    # Print the header row
    print(" " * 5, end="")  # Initial space for table alignment
    for i in range(2, 13):
        print(f"{i:>4}", end="")  # Print numbers from 2 to 12
    print()  # Newline after header

    # Print a separator line
    print(" " * 5 + "----" * 11)  # Aligning the separator

    # Iterate through rows (2 to 12)
    for row in range(2, 13):
        # Print the row label
        print(f"{row}|", end="")  # Row label

        # Iterate through columns (2 to 12)
        for col in range(2, 13):
            product = row * col
            print(f"{product:>4}", end="")  # Print formatted product
        print()  # Move to the next line after printing a row

# Call the function to print the multiplication table
print_multiplication_table()
