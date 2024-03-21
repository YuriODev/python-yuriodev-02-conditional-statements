# Prompt the user to enter a three-digit number
number = int(input("Enter a three-digit number: "))

# Extract the first, second, and third digits of the number
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

# Calculate the sum of the first and third digits
sum_comparison = first_digit + third_digit

# Compare the sum with the second digit and print the result
if sum_comparison > second_digit:
    print(">")
elif sum_comparison < second_digit:
    print("<")
else:
    print("=")
