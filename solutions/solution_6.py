x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))

distance_a = x1**2 + y1**2
distance_b = x2**2 + y2**2

if distance_a > distance_b:
    print("A is further from the origin.")
elif distance_a < distance_b:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")
