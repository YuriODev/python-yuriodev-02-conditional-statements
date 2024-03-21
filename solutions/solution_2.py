# Prompt the user to enter their age and convert it to an integer
age = int(input("Enter your age: "))


# Check the age of the user and print an appropriate message
if age <= 1:
    # If the age is less than or equal to 1, the user is an infant
    print("You are an infant.")
# If the age is greater than 1 and less than 13, the user is a child
elif age < 13:
    # If the age is less than 13, the user is a child
    print("You are a child.")
elif age < 20:
    # If the age is less than 20, the user is a teenager
    print("You are a teenager.")
else:
    # If the age is 20 or greater, the user is an adult
    print("You are an adult.")
