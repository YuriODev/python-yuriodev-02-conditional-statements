
number = int(input("Enter a number (0-36): "))

if number == 0:
    print("Green")
elif 1 <= number <= 10 or 19 <= number <= 28:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif 11 <= number <= 18 or 29 <= number <= 36:
    if number % 2 == 0:
        print("Red")
    else:
        print("Black")
else:
    print("The bet will not play!")
