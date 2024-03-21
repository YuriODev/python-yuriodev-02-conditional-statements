# Prompt the user to enter Alex's age
age_alex = int(input("Enter Alex's age: "))

# Prompt the user to enter Tatyana's age
age_tatyana = int(input("Enter Tatyana's age: "))

# Compare the ages and print the result
if age_alex > age_tatyana:
    # If Alex's age is greater than Tatyana's age
    print("Alex is the eldest.")
# If Alex's age is less than Tatyana's age
elif age_alex < age_tatyana:
    print("Tatyana is the eldest.")
# If Alex's age is equal to Tatyana's age
else:
    print("Alex and Tatyana are of the same age.")