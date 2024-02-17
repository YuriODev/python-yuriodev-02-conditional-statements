<<<<<<< HEAD

number = int(input("Enter a three-digit number: "))

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

sum_comparison = first_digit + third_digit

if sum_comparison > second_digit:
    print(">")
elif sum_comparison < second_digit:
    print("<")
else:
    print("=")
=======
# Your solution to Exercise 9

>>>>>>> e2be20ee77cdbae9a6d1e5effe3c3653928557aa
