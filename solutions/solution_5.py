a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

output = "No roots."

if a == 0:
    if b != 0:
        output = f"{-c / b}"
elif b == 0:
    if c != 0:
        if -c / a >= 0:
            x1 = (-c / a) ** 0.5
            x2 = -(-c / a) ** 0.5
            output = f"{x1} and {x2}"
    else:
        output = "0"
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        output = f"{x1} and {x2}"
    elif d == 0:
        x = -b / (2 * a)
        output = f"{x}"

print(output)
