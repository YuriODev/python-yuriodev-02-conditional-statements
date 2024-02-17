# Input: A four-digit number
number = int(input("Enter a four-digit number: "))

# Process each digit and replace even digits with '*'
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

# Check each digit and replace if necessary
thousands = '*' if thousands % 2 == 0 else str(thousands)
hundreds = '*' if hundreds % 2 == 0 else str(hundreds)
tens = '*' if tens % 2 == 0 else str(tens)
ones = '*' if ones % 2 == 0 else str(ones)

# Combine the digits back into a string
result = thousands + hundreds + tens + ones

# Output the result
print(result)
