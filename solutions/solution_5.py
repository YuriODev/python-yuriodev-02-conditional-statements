# Prompt the user to enter coefficient a and convert it to a float
a = float(input("Enter coefficient a: "))

# Prompt the user to enter coefficient b and convert it to a float
b = float(input("Enter coefficient b: "))

# Prompt the user to enter coefficient c and convert it to a float
c = float(input("Enter coefficient c: "))

# Initialize the output variable with the default value "No roots."
output = "No roots."

# Check if all coefficients are zero
if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."

# Check if coefficient a is equal to 0
elif a == 0:
    # If coefficient a is 0, check if coefficient b is not equal to 0
    if b != 0:
        # If coefficient b is not 0, calculate the root
        # using the formula -c / b
        output = f"{-c / b}"

# If coefficient a is not 0, check if coefficient b is equal to 0
elif b == 0:
    # If coefficient b is 0, check if coefficient c is not equal to 0
    if c != 0:
        # If coefficient c is not 0 and -c / a is greater than or equal to 0,
        # calculate the roots using the formula (-c / a) ** 0.5 and
        #  -(-c / a) ** 0.5
        x1 = (-c / a) ** 0.5
        x2 = -(-c / a) ** 0.5
        output = f"{x1} and {x2}"
    else:
        # If coefficient c is 0, set the output to "0"
        output = "0"

# If neither coefficient a nor b is 0, calculate the discriminant d
else:
    d = b ** 2 - 4 * a * c

    # Check if the discriminant d is greater than 0
    if d > 0:
        # If d is greater than 0, calculate the roots using
        # the quadratic formula
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        output = f"{x1} and {x2}"

    # Check if the discriminant d is equal to 0
    elif d == 0:
        # If d is equal to 0, calculate the root using the formula -b / (2 * a)
        x = -b / (2 * a)
        output = f"{x}"

# Print the output
print(output)
