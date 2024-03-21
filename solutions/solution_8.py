# Prompt the user to enter a three-digit number and store it in the variable 'number'
number = int(input("Enter a three-digit number: "))

# Prompt the user to enter a digit and store it in the variable 'digit'
digit = int(input("Enter a digit: "))

# Check if the entered digit is present in the three-digit number
# The expression digit == number % 10 checks if the digit is equal to the last digit of the number
# The expression digit == (number // 10) % 10 checks if the digit is equal to the middle digit of the number
# The expression digit == number // 100 checks if the digit is equal to the first digit of the number
is_in_number = digit == number % 10 or digit == (number // 10) % 10 or digit == number // 100

# Print whether the digit is present in the number
print(is_in_number)
