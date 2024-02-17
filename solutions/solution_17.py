# Input: Six-digit ticket number
ticket_number = int(input("Enter a six-digit ticket number: "))

# Extract digits using division and modulo
digit1 = ticket_number // 100000
digit2 = (ticket_number // 10000) % 10
digit3 = (ticket_number // 1000) % 10
digit4 = (ticket_number // 100) % 10
digit5 = (ticket_number // 10) % 10
digit6 = ticket_number % 10

# Calculate sums of the first three and the last three digits
sum_first_three = digit1 + digit2 + digit3
sum_last_three = digit4 + digit5 + digit6

# Determine if the ticket is lucky
if sum_first_three == sum_last_three:
    output = "Happy"
else:
    output = "Ordinary"

# Output the result
print(output)
