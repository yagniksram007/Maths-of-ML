def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome!")
