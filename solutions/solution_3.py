# Prompt the user to enter a number between 0 and 36
number = int(input("Enter a number (0-36): "))

# Initialize the output variable to "The bet will play!"
output = "The bet will not play!"

# Check the number entered and determine the color of the bet
if number == 0:
    output = "Green"
# Check if the number is in the range of 1-10 or 19-28
elif 1 <= number <= 10 or 19 <= number <= 28:
    # If the number is odd, the color is Black, otherwise, it's Red
    output = "Red" if number % 2 else "Black"
# Check if the number is in the range of 11-18 or 29-36
elif 11 <= number <= 18 or 29 <= number <= 36:
    # If the number is odd, the color is Red, otherwise, it's Black
    output = "Black" if number % 2 else "Red"

# Print the color of the bet
print(output)
