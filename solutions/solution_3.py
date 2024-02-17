number = int(input("Enter a number (0-36): "))

output = "The bet will play!"

if number == 0:
    output = "Green"
elif 1 <= number <= 10 or 19 <= number <= 28:
    output = "Black" if number % 2 else "Red"
elif 11 <= number <= 18 or 29 <= number <= 36:
    output = "Red" if number % 2 else "Black"

print(output)
