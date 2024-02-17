# Input: Current date (day, month, year)
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Initialize output variable
output = ""

# Check for leap year
is_leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# February and leap year logic
if month == 2:
    if is_leap_year and day == 29:
        day = 1
        month = 3
    elif not is_leap_year and day == 28:
        day = 1
        month = 3
    elif day < 28 or (is_leap_year and day < 29):
        day += 1
    else:
        output = "Invalid date"

# Months with 31 days
elif month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10:
    if day == 31:
        day = 1
        month += 1
    elif day < 31:
        day += 1
    else:
        output = "Invalid date"

# December to January transition
elif month == 12:
    if day == 31:
        day = 1
        month = 1
        year += 1
    elif day < 31:
        day += 1
    else:
        output = "Invalid date"

# Months with 30 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1
    elif day < 30:
        day += 1
    else:
        output = "Invalid date"

else:
    output = "Invalid date"

# Prepare the output message if the date is valid
if output == "":
    output = f"{day}.{month}.{year}"

# Output the next day's date, if valid
print(output)
