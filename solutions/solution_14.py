# Input: A four-digit number
number = int(input("Enter a four-digit number: "))

# Extract digits
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

# Check if the number is a palindrome
is_palindrome = (thousands == ones) and (hundreds == tens)

# Output the result
print(is_palindrome)
