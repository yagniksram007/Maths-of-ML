def print_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        
rows = int(input("Enter the number of rows (n): "))
print_number_pattern(rows)
