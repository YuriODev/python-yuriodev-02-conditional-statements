# Examples 👨🏼‍💻

Here are some examples to get you started.

**Covered topics:** 
- **Branching** (Conditional Statements)

## Example 1: Temperature Feedback Messages
**Problem:** Write a program where the user enters a temperature value, and if this value is less than or equal to `0` degrees Celsius, you need to display the message "A cold, isn’t it?". If the temperature is more than `0` and less than `10` degrees Celsius, the message will be "Cool.". In other cases, "Nice weather we’re having.".

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 12.5   | Nice weather we're having.      |
| 2   | -5     | A cold, isn't it?               |
| 3   | 9      | Cool.                           |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Temperature value from the user
temperature = float(input("Enter temperature in degrees Celsius: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to check the temperature and assign appropriate messages
if temperature <= 0:
    output = "A cold, isn't it?"
elif temperature > 0 and temperature < 10:
    output = "Cool."
else:
    output = "Nice weather we're having."

# Print the output message
print(output)
```
</details>

## Example 2: Football Match Scoring
**Problem:** In a football championship, a team is given `3` points for a win, `0` for a loss, and `1` for a draw. The number of points received by the team for the game is known. Display the result of the game in the form of corresponding words: "win", "loss", or "draw".

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | win     |
| 2   | 1      | draw    |
| 3   | 0      | lose    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Number of points received by the team
points = int(input("Enter the number of points: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the match result and assign it to the output variable
if points == 3:
    output = "win"
elif points == 1:
    output = "draw"
elif points == 0:
    output = "lose"

# Print the output message
print(output)
```
</details>

## Example 3: Positive, Negative, or Zero Determination
**Problem:** Determine whether an entered number is positive, negative, or zero.

| No. | Inputs | Outputs                |
| --- | ------ | ---------------------- |
| 1   | 7      | It is a positive number|
| 2   | -5.6   | It is a negative number|
| 3   | 0      | It is Zero             |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: A number from the user
number = float(input("Enter a number: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the nature of the number and assign an appropriate message
if number > 0:
    output = "It is a positive number"
elif number < 0:
    output = "It is a negative number"
else:
    output = "It is Zero"

# Print the output message
print(output)
```
</details>

## Example 4: Spacecraft Trajectory
**Problem:** Write a program that determines the behavior of a spacecraft launching at the equator, depending on its initial speed `v`, given in km/s (real numbers). There are four possible cases: 
- if `v < 7.8` km/s, the device will fall to the Earth's surface; 
- if `7.8 ≤ v < 11.2` km/s, the device will become a satellite of the Earth; 
- if `11.2 ≤ v < 16.4` km/s, the device will become a satellite of the Sun; 
- if `v ≥ 16.4` km/s, the spacecraft will leave the Solar System.

| No. | Inputs | Outputs                               |
| --- | ------ | ------------------------------------- |
| 1   | 12.5   | The device will become a satellite of the Sun. |
| 2   | 8.3    | The device will become a satellite of the Earth. |
| 3   | 0      | The device will fall to the Earth's surface. |
| 4   | 20     | The device will leave the Solar System. |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Initial speed of the spacecraft in km/s
v = float(input("Enter the spacecraft's initial speed in km/s: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the spacecraft's trajectory
if v < 7.8:
    output = "The device will fall to the Earth's surface."
elif 7.8 <= v < 11.2:
    output = "The device will become a satellite of the Earth."
elif 11.2 <= v < 16.4:
    output = "The device will become a satellite of the Sun."
else:
    output = "The device will leave the Solar System."

# Print the output message
print(output)
```
</details>

## Example 5: Grading System Interpretation
**Problem:** The university uses the following scale to interpret student test results: 
- `90` points and above (A), 
- `80-89` (B), 
- `70-79` (C), 
- `60-69` (D), 
- below `60` (F). 

Write a program that allows the student to enter the test score, and then display the grade for this score.

| No. | Inputs | Outputs             |
| --- | ------ | ------------------- |
| 1   | 95     | Your grade is A.    |
| 2   | 74     | Your grade is C.    |
| 3   | 60     | Your grade is D.    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Student's test score
score = int(input("Enter the test score: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to determine the grade
if score >= 90:
    output = "Your grade is A."
elif score >= 80:
    output = "Your grade is B."
elif score >= 70:
    output = "Your grade is C."
elif score >= 60:
    output = "Your grade is D."
else:
    output = "Your grade is F."

# Print the output message
print(output)
```
</details>

## Example 6: Day of the Week Determination
**Problem:** Determine the day of the week based on a number entered by the user.

| No. | Inputs | Outputs                      |
| --- | ------ | ---------------------------- |
| 1   | 5      | Friday                       |
| 2   | 2      | Tuesday                      |
| 3   | 7      | Sunday                       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Number representing a day of the week
day_number = int(input("Enter the day number: "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to assign the name of the day
if day_number == 1:
    output = "Monday"
elif day_number == 2:
    output = "Tuesday"
elif day_number == 3:
    output = "Wednesday"
elif day_number == 4:
    output = "Thursday"
elif day_number == 5:
    output = "Friday"
elif day_number == 6:
    output = "Saturday"
elif day_number == 7:
    output = "Sunday"
else:
    output = "Invalid day number"

# Print the output message
print(output)
```
</details>

## Example 7: Magic date

**Problem:** We will call the date October 2, 2020, "magic" because when it is written in the format `02.10.20`, the product of the day and month values equals the year value. Write a program that asks the user to enter the day, month, and year (only the last two digits) in numerical form. The program should output a message that the entered date is "magic". Otherwise, there should be a message that it is a regular date.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>10<br>20 | The date is magic! |
| 2   | 3<br>11<br>21 | The date is not magic. |
| 3   | 1<br>1<br>21  | The date is not magic. |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Day, month, and year (last two digits) from the user
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the last two digits of the year: "))

# Initialize an empty string for the output message
output = ""

# Check if the product of day and month equals the year
if day * month == year:
    output = "The date is magic!"
else:
    output = "The date is not magic."

# Print the output message
print(output)
```
</details>


## Example 8: Roman Numeral Conversion
**Problem:** Convert a decimal number within 1 to 10 into its Roman numeral equivalent.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 8      | VIII    |
| 2   | 10     | X       |
| 3   | 4      | IV      |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Decimal number from the user
decimal = int(input("Enter a decimal number (1-10): "))

# Initialize an empty string for the output message
output = ""

# Conditional statements to convert decimal number to Roman numeral
if decimal == 1:
    output = "I"
elif decimal == 2:
    output = "II"
elif decimal == 3:
    output = "III"
elif decimal == 4:
    output = "IV"
elif decimal == 5:
    output = "V"
elif decimal == 6:
    output = "VI"
elif decimal == 7:
    output = "VII"
elif decimal == 8:
    output = "VIII"
elif decimal == 9:
    output = "IX"
elif decimal == 10:
    output = "X"
else:
    output = "Invalid number"

# Print the output message
print(output)
```
</details>

## Example 9: Software Package Discount Calculation
**Problem:** A software manufacturer in the field of information security sells one set of programs for £2700. If multiple units of goods are purchased, a discount system works: 
- `10-19` units of goods - `10%`, 
- `20-49` - `20%`, 
- `50-99` - `30%`, 
- `100` or more - `40%`. 

Write a program that receives from the user an integer - the number of purchased software sets and outputs a message about the amount of the discount (if any) and the total amount of the purchase with the discount.

| No. | Inputs | Outputs                                                   |
| --- | ------ | --------------------------------------------------------- |
| 1   | 26     | The amount of discount is 20%, total amount of the purchase after the discount is £56160.00 |
| 2 | 3 | The amount of discount is 0%, total amount of the purchase after the discount is £8100.00 |
| 3 | 110 | The amount of discount is 40%, total amount of the purchase after the discount is £178200.00 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Number of purchased software sets from the user
units = int(input("Enter the number of software sets purchased: "))

# Initialize variables for the discount percentage and cost per unit
cost_per_unit = 2700
discount_percentage = 0

# Determine the discount percentage based on the number of units
if 10 <= units <= 19:
    discount_percentage = 10
elif 20 <= units <= 49:
    discount_percentage = 20
elif 50 <= units <= 99:
    discount_percentage = 30
elif units >= 100:
    discount_percentage = 40

# Calculate total cost after discount
total_cost = units * cost_per_unit * (1 - discount_percentage / 100)

# Prepare the output message
output = f"The amount of discount is {discount_percentage}%, total amount of the purchase after the discount is £{total_cost:.2f}"

# Print the output message
print(output)
```
</details>


## Example 10: Days in a Month
**Problem:** Output the number of days in a given month.

| No. | Inputs   | Outputs                     |
| --- | -------- | --------------------------- |
| 1   | February | February has 28 or 29 days in it. |
| 2   | April    | April has 30 days in it.    |
| 3   | December | December has 31 days in it. |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Name of the month from the user
month = input("Enter the name of the month: ")

# Initialize an empty string for the output message
output = ""

# Determine the number of days in the month using if-else
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    output = f"{month} has 31 days in it."
elif month == "April" or month == "June" or month == "September" or month == "November":
    output = f"{month} has 30 days in it."
elif month == "February":
    output = "February has 28 or 29 days in it."
else:
    output = "Invalid month name"

# Print the output message
print(output)
```
</details>

## Example 11: Tax Calculation Based on Brackets
**Problem:** Depending on the size of the amount, the tax from it is calculated according to the following scheme: 
- if the amount does not exceed a certain value `a`, then the tax is not calculated; 
- if the amount is greater than `a` but does not exceed `b`, then the tax is `10%`; 
- if the amount is greater than `b` but does not exceed `c`, then the tax is `25%`; 
- if the amount is greater than `c`, then the tax is `50%`. 

Determine what tax (real number) will be calculated from the amount of size `s`. The data (integers) are entered in the following order: `a`, `b`, `c`, `s`.

| No. | Inputs | Outputs                        |
| --- | ------ | ------------------------------ |
| 1   | 1000<br>10000<br>100000<br>15000 | 1500.0 |
| 2   | 1000<br>10000<br>100000<br>5000  | 500.0  |
| 3   | 1000<br>10000<br>100000<br>500000 | 250000.0 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Tax brackets and size of the amount from the user
a = int(input("Enter the lower limit of the tax bracket: "))
b = int(input("Enter the middle limit of the tax bracket: "))
c = int(input("Enter the upper limit of the tax bracket: "))
s = int(input("Enter the size of the amount: "))

# Initialize a variable for the tax amount
tax = 0

# Determine the tax based on the amount
if s <= a:
    tax = 0
elif a < s <= b:
    tax = s * 0.1
elif b < s <= c:
    tax = s * 0.25
else:
    tax = s * 0.5

# Prepare the output message
output = f"The tax calculated from the amount is {tax:.2f}"

# Print the output message
print(output)
```
</details>


## Example 12: Ending with 5 Determination
**Problem:** Determine if a given number ends with the digit 5.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12395  | True    |
| 2   | 123    | False   |
| 3   | 0      | False   |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: A number from the user
number = int(input("Enter a number: "))

# Determine if the number ends with 5
if number % 10 == 5:
    output = "True"
else:
    output = "False"

# Print the output message
print(output)
```
</details>

## Example 13: Roulette Color Prediction
**Problem:** Given a two-digit number. Determine which of its digits is larger: 
- the first (output `1`) 
- or the second (output `2`), 
- or the digits are equal (output `=`).
- If the number is less than `10` or greater than `99`, output `0`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 23     | 2       |
| 2   | 37     | 2       |
| 3   | 22     | =       |
| 4   | 10     | 1       |
| 5   | -1    | 0       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: A two-digit number from the user
number = int(input("Enter a two-digit number: "))

# Check if the number is within the valid range
if number < 10 or number > 99:
    output = "0"
else:
    # Extract digits
    first_digit = number // 10
    second_digit = number % 10
    
    # Compare digits
    if first_digit > second_digit:
        output = "1"
    elif second_digit > first_digit:
        output = "2"
    else:
        output = "="

# Print the output message
print(output)
```
</details>

## Example 14: Overtime Pay Calculation
**Problem:** Several workers work at the car repair station. If any worker works more than `40` hours a week, he receives `1.5` times more than the usual hourly pay. Develop a program that calculates the employee's salary, including payment for extra hours. The program receives two integers - the number of working hours and the hourly rate.

| No. | Inputs | Outputs     |
| --- | ------ | ----------- |
| 1   | 45     | 712.5       |
| 2   | 35     | 560.0       |
| 3   | 50     | 875.0       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Number of working hours and hourly rate from the user
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

# Initialize the pay variable
pay = 0

# Calculate pay with overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    pay = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
else:
    pay = hours_worked * hourly_rate

# Prepare the output message
output = f"The total pay is {pay:.2f}"

# Print the output message
print(output)
```
</details>

## Example 15: Circle Belonging Determination
**Problem:** The coordinates `(x, y)` of point `A` and the radius of the circle `(r)` are entered. Determine whether the given point belongs to the circle if its center is at the origin.

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 3<br>4   | The point belongs to the circle |
| 2   | -2<br>5  | The point is outside the circle |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Coordinates of point A (x, y) and the circle's radius r
x = float(input("Enter the x coordinate of point A: "))
y = float(input("Enter the y coordinate of point A: "))
r = float(input("Enter the radius of the circle: "))

# Determine whether the point belongs to the circle centered at the origin
if x**2 + y**2 <= r**2:
    output = "The point belongs to the circle"
else:
    output = "The point is outside the circle"

# Print the output message
print(output)
```
</details>

## Example 16: Coordinate Quarter Determination
**Problem:** Determine the quarter of the coordinate plane a point belongs to.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>-4  | IV      |
| 2   | -4<br>3  | II      |
| 3   | 0<br>0   | The point is at the origin |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Coordinates of a point (x, y)
x = float(input("Enter the x coordinate of the point: "))
y = float(input("Enter the y coordinate of the point: "))

# Determine the coordinate quarter
if x > 0 and y > 0:
    output = "I"
elif x < 0 and y > 0:
    output = "II"
elif x < 0 and y < 0:
    output = "III"
elif x > 0 and y < 0:
    output = "IV"
elif x == 0 and y == 0:
    output = "The point is at the origin"
else:
    output = "The point lies on an axis, not strictly in a quarter"

# Print the output message
print(output)
```
</details>

## Example 17: Body Mass Index and Categorization
**Problem:** Write a program to calculate the body mass index, which is calculated by the formula: `index = mass / (height * height)`. The user enters the values of height (in meters) and mass (in kilograms), and the program calculates the body mass index and outputs the corresponding message: 
- `underweight` (low mass, index less than `18.5`), 
- `normal weight` (normal mass, index `18.5-24.9`), 
- `overweight` (excessive mass, index more than `24.9`).

| No. | Inputs      | Outputs                                       |
| --- | ----------- | --------------------------------------------- |
| 1   | 1.79<br>88    | Your body mass index is: 27.46, that is overweight. |
| 2   | 1.90<br>85    | Your body mass index is: 23.55, that is normal weight. |
| 3   | 1.60<br>50    | Your body mass index is: 19.53, that is normal weight. |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Height (in meters) and mass (in kilograms)
height = float(input("Enter your height in meters: "))
mass = float(input("Enter your mass in kilograms: "))

# Calculate the Body Mass Index (BMI)
bmi = mass / (height ** 2)

# Categorize the BMI
if bmi < 18.5:
    output = f"Your body mass index is: {bmi:.2f}, that is underweight."
elif 18.5 <= bmi <= 24.9:
    output = f"Your body mass index is: {bmi:.2f}, that is normal weight."
elif bmi > 24.9:
    output = f"Your body mass index is: {bmi:.2f}, that is overweight."

# Print the output message
print(output)
```
</details>

## Example 18: Chessboard Cell Color Matching
**Problem:** Two cells of a chessboard are given. If they are painted in one color, then print the word `Yes`, and if in different colors - `No`. The program receives four numbers from `1` to `8` each, which set the column number and the row number first for the first cell, then for the second cell.

| No. | Inputs    | Outputs |
| --- | --------- | ------- |
| 1   | 1<br>1<br>2<br>2 | No  |
| 2   | 1<br>1<br>1<br>2 | Yes |
| 3   | 1<br>1<br>2<br>1 | Yes |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Column and row numbers for two cells on a chessboard
column1 = int(input("Enter the column number of the first cell: "))
row1 = int(input("Enter the row number of the first cell: "))
column2 = int(input("Enter the column number of the second cell: "))
row2 = int(input("Enter the row number of the second cell: "))

# Determine the color of each cell (even+even or odd+odd are black; otherwise white)
cell1_color = (column1 + row1) % 2
cell2_color = (column2 + row2) % 2

# Check if both cells are of the same color
if cell1_color == cell2_color:
    output = "Yes"
else:
    output = "No"

# Print the output message
print(output)
```
</details>

## Example 19: Triangle Type Determination
**Problem:** Given three sides of a triangle `a`, `b`, `c`. Determine the type of triangle with the given sides. Print one of four words: 
- `rectangular` for a right triangle, 
- `acute` for an acute triangle, 
- `obtuse` for an obtuse triangle, 
- or `impossible` if there is no triangle with such sides.Determine the type of a triangle based on its angles.

| No. | Inputs | Outputs   |
| --- | ------ | --------- |
| 1   | 3<br>4<br>5 | rectangular |
| 2   | 3<br>4<br>6 | obtuse      |
| 3   | 3<br>4<br>7 | impossible  |
| 4   | 3<br>4<br>4 | acute       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Three sides of a triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Initialize the output variable
output = ""

# Check for triangle impossibility first
if a + b <= c or a + c <= b or b + c <= a:
    output = "impossible"
else:
    # Use the squares of the sides to determine the triangle type without sorting
    a2, b2, c2 = a**2, b**2, c**2
    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        output = "rectangular"
    elif a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
        output = "acute"
    else:
        output = "obtuse"

# Print the output message
print(output)
```
</details>

## Example 20: Identical Digits Counting
**Problem:** Given a three-digit integer. Determine the number of identical digits in the number record and output the value of this quantity.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 123    | 0       |
| 2   | 111    | 3       |
| 3   | 121    | 2       |
| 4   | 100    | 1       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: A three-digit integer
number = int(input("Enter a three-digit number: "))

# Extract digits
first_digit = number // 100
second_digit = (number % 100) // 10
third_digit = number % 10

# Initialize count
count = 0

# Count identical digits using direct comparison
if first_digit == second_digit == third_digit:
    count = 3
elif first_digit == second_digit or first_digit == third_digit or second_digit == third_digit:
    count = 2

# Prepare the output message
output = f"{count}"

# Print the output message
print(output)
```
</details>

## Example 21: Next Day Date Validation
**Problem:** Write a program in which the user enters the value of the current date: day, month, and year (integer numbers), and the program outputs tomorrow's date in the format: `dd.mm.yyyy`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>1<br>2020 | 02.01.2020 |
| 2   | 28<br>2<br>2020 | 29.02.2020 |
| 3   | 31<br>12<br>2020 | 01.01.2021 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Input: Current date (day, month, year)
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Check for leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Initialize output message
output = ""

# Manually handle each month's end-of-month logic
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day < 31:
        day += 1
    else:  # Last day of the month
        day = 1
        month += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 30:
        day += 1
    else:  # Last day of the month
        day = 1
        month += 1
elif month == 2:
    # Check for leap year
    if is_leap:
        if day < 29:
            day += 1
        else:  # Last day of February in a leap year
            day = 1
            month += 1
    else:  # Not a leap year
        if day < 28:
            day += 1
        else:
            day = 1
            month += 1
elif month == 12:
    if day < 31:
        day += 1
    else:  # Transition to the next year
        day = 1
        month = 1
        year += 1
else:
    output = "Invalid date provided."

# Prepare the output message if it's not set to "Invalid date provided."
if output == "":
    output = f"Next day's date: {day:02d}.{month:02d}.{year}"

# Print the output message
print(output)
```
</details>


#

**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.