def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example 
num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
