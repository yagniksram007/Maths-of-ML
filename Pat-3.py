def print_kite_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n * 2):
            if j >= n - i + 1 and j <= n + i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(1, n * 2):
            if j >= n - i + 1 and j <= n + i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example: n = 5
n = int(input("Enter the size of the kite (n): "))
print_kite_pattern(n)
