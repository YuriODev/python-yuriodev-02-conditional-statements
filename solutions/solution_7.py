# Prompt the user to enter the first number and store it in the variable num1
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and store it in the variable num2
num2 = float(input("Enter the second number: "))

# Prompt the user to enter the operation they want to perform and store it in the variable operation
operation = input("Enter the operation (+, -, *, /, mod, pow, div): ")

# Check if the operation is addition
if operation == "+":
    # If it is, perform the addition and store the result in the variable result
    result = num1 + num2

# Check if the operation is subtraction
elif operation == "-":
    # If it is, perform the subtraction and store the result in the variable result
    result = num1 - num2

# Check if the operation is multiplication
elif operation == "*":
    # If it is, perform the multiplication and store the result in the variable result
    result = num1 * num2

# Check if the operation is division
elif operation == "/":
    # If it is, check if the second number is not zero
    if num2 != 0:
        # If it's not zero, perform the division and store the result in the variable result
        result = num1 / num2
    else:
        # If it is zero, set the result to "Division by 0!"
        result = "Division by 0!"

# Check if the operation is modulo
elif operation == "mod":
    # If it is, check if the second number is not zero
    if num2 != 0:
        # If it's not zero, perform the modulo operation and store the result in the variable result
        result = num1 % num2
    else:
        # If it is zero, set the result to "Division by 0!"
        result = "Division by 0!"

# Check if the operation is exponentiation
elif operation == "pow":
    # If it is, perform the exponentiation and store the result in the variable result
    result = num1 ** num2

# Check if the operation is floor division
elif operation == "div":
    # If it is, check if the second number is not zero
    if num2 != 0:
        # If it's not zero, perform the floor division and store the result in the variable result
        result = num1 // num2
    else:
        # If it is zero, set the result to "Division by 0!"
        result = "Division by 0!"

# If none of the above conditions are met, set the result to "Invalid operation"
else:
    result = "Invalid operation"

# Print the result
print(result)
