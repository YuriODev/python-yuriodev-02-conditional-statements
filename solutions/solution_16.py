# Input: Current date (day, month, year)
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Determine if it's a leap year
is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Adjust for the previous day
if day == 1:
    if month == 1:
        day = 31
        month = 12
        year -= 1
    elif month == 3:
        day = 29 if is_leap_year else 28
        month = 2
    elif month == 5 or month == 7 or month == 10 or month == 12:
        day = 30
        month -= 1
    elif month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
        day = 31
        month -= 1
else:
    day -= 1

# Prepare the output message
output = f"{day:02d}.{month:02d}.{year}"

# Output the previous day's date
print(output)
