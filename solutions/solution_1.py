age_alex = int(input("Enter Alex's age: "))
age_tatyana = int(input("Enter Tatyana's age: "))

if age_alex > age_tatyana:
    print("Alex is the eldest.")
elif age_alex < age_tatyana:
    print("Tatyana is the eldest.")
else:
    print("Alex and Tatyana are of the same age.")