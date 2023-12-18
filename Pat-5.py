def print_rectangle_pattern(n):
    for i in range(n):
        print("A", end=" ")
        for j in range(n - 1):
            print("AB", end=" ")
        print("A")

# Example: n = 3
n = int(input("Enter the value of n: "))
print_rectangle_pattern(n)
