# Input: Student's test score
score = int(input("Enter the test score: "))


# Conditional statements to determine the grade
if 0 < score <= 100:
    # Initialize an empty string for the output message
    output = ""
    
    if score >= 90:
        output = "A"
    # elif 80 < score < 90:
    # elif score < 90 and score >= 80:
    elif score >= 80:
        output = "B"
    elif score >= 70:
        output = "C"
    elif score >= 60:
        output = "D"
    else:
        output = "F"

    # Print the output message
    print(f"Your grade is {output}.")
else:
    print("The entered score is invalid")
