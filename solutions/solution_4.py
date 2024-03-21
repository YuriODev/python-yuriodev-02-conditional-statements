# Prompt the user to enter a grade and convert it to an integer
grade = int(input("Enter the school grade (1-12): "))

# Check the grade and print the corresponding level
if 1 <= grade <= 3:
    print("initial level")

# If the grade is between 4 and 6 (inclusive)
elif grade <= 6:
    print("average level")

# If the grade is between 7 and 9 (inclusive)
elif grade <= 9:
    print("sufficient level")

# If the grade is between 10 and 12 (inclusive)
elif grade <= 12:
    print("high level")

# If the grade is not within the range of 1-12
else:
    print("level is absent")
