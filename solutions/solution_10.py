
# Prompt the user to enter the coordinates of three points
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))

# Calculate the squares of the distances between the points
a2 = (x2-x1)**2 + (y2-y1)**2
b2 = (x3-x2)**2 + (y3-y2)**2
c2 = (x1-x3)**2 + (y1-y3)**2

# Check if any of the sides of the triangle is equal to 0
# We can use the Pythagorean theorem to check if the triangle is right-angled
# a2 + b2 == c2 or b2 + c2 == a2 or c2 + a2 == b2
# If any of these conditions is True, then the triangle is right-angled
# Otherwise, it is not

if a2 == 0 or b2 == 0 or c2 == 0:
    print("No")
elif a2 + b2 == c2 or b2 + c2 == a2 or c2 + a2 == b2:
    print("Yes")
else:
    print("No")
