# Predefined outcomes as constants
SAY_HI = "Say hi."
DONT_SAY_HI = "Don't say hi."
RUN_FOR_IT = "Run for it."
KEEP_WALKING = "Keep walking."
ADDRESS_WITH_NICKNAME = "Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster.'"
HELLO_DOCTOR = "Hello, doctor. What are my test results?"

# Start of the decision tree
remember_name = input("Do you remember the person's name? (yes/no): ").lower()

if remember_name == 'yes':
    is_ex = input("Is it an ex? (yes/no): ").lower()
    if is_ex == 'yes':
        are_you_drunk = input("Are you drunk? (yes/no): ").lower()
        if are_you_drunk == 'yes':
            rekindle = input("Do you want to rekindle and/or give 'em what for? (yes/no): ").lower()
            output = SAY_HI if rekindle == 'yes' else DONT_SAY_HI
        else:
            in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no): ").lower()
            output = SAY_HI if in_convertible == 'yes' else DONT_SAY_HI
    else:
        friend_ex = input("A friend's ex? (yes/no): ").lower()
        if friend_ex == 'yes':
            output = DONT_SAY_HI
        else:
            enemy_or_frenemy = input("An enemy or frenemy? (yes/no): ").lower()
            if enemy_or_frenemy == 'yes':
                in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no): ").lower()
                output = SAY_HI if in_convertible == 'yes' else DONT_SAY_HI
            else:
                robbing_bank = input("Are you robbing a bank? (yes/no): ").lower()
                if robbing_bank == 'yes':
                    output = DONT_SAY_HI
                else:
                    in_bathrobe = input("Are you in a bathrobe? (yes/no): ").lower()
                    output = DONT_SAY_HI if in_bathrobe == 'yes' else SAY_HI

else:  # Don't remember the person's name
    time_to_flee = input("Is there time to flee? (yes/no): ").lower()
    if time_to_flee == 'yes':
        output = RUN_FOR_IT
    else:
        pretend_call = input("Could you pretend to get a call on your cell? (yes/no): ").lower()
        if pretend_call == 'yes':
            output = HELLO_DOCTOR
        else:
            wearing_sunglasses = input("Are you wearing sunglasses? (yes/no): ").lower()
            if wearing_sunglasses == 'yes':
                output = KEEP_WALKING
            else:
                output = ADDRESS_WITH_NICKNAME

print(output)
