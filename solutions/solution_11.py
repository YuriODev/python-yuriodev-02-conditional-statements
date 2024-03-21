# Prompt user to enter a year and determine if it is a leap year or not.
year = int(input("Enter a year: "))


# Check if the year is divisible by 4 and not divisible by 100, or if it is divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Ordinary year.")
