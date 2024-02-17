number = int(input("Enter a three-digit number: "))
digit = int(input("Enter a digit: "))

is_in_number = digit == number % 10 or digit == (number // 10) % 10 or digit == number // 100

print(is_in_number)
