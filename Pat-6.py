def print_custom_pattern():
    pattern1 = ['A', 'B', 'C', 'D', 'A']
    pattern2 = ['A', ' ' * 9, 'A']
    pattern3 = ['A', 'E', 'F', 'G', 'A']
    
    rows = int(input("Enter the number of rows: "))
    
    for i in range(rows):
        for char in pattern1:
            print(char, end=" ")
        print()

    for i in range(rows):
        for char in pattern2:
            print(char, end=" ")
        print()

    for i in range(rows):
        for char in pattern3:
            print(char, end=" ")
        print()

# Example: rows = 2
print_custom_pattern()
