def print_custom_pattern(rows):
    for i in range(rows):
        if i % 2 == 0:
            print(" A" * (i // 2 + 1))
        else:
            print("A" + " " * (2 * (rows - i) - 3) + "A")

# Example: rows = 5
rows = int(input("Enter the number of rows: "))
print_custom_pattern(rows)
