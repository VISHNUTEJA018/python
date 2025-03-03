import string

# Input string from the user
input_string = input("Enter a string: ")

# Initialize counters for uppercase, lowercase, and special characters
uppercase_count = 0
lowercase_count = 0
special_count = 0
cleaned_string = ''

# Loop through each character in the input string
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char in string.punctuation:  # Check for special characters
        special_count += 1
    else:
        cleaned_string += char  # Keep the character if it's not special

# Remove special characters from the input string
updated_string = ''.join([char for char in input_string if char not in string.punctuation])

# Print the result in a formatted table
print(f"{'Category':<20}{'Count'}")
print(f"{'-' * 25}")
print(f"{'Uppercase characters':<20}{uppercase_count}")
print(f"{'Lowercase characters':<20}{lowercase_count}")
print(f"{'Special characters':<20}{special_count}")
print(f"{'Updated string':<20}{updated_string}")
print(f"{'Cleaned string (no special chars)':<20}{cleaned_string}")
