try:
    age = int(input("Enter your age: "))

    # Outer condition: Check if the age is at least 10
    if age >= 10:
        # Inner (nested) condition: Check if it is also 20 or less
        if age <= 20:
            print("The age is between 10 and 20.")
        else:
            print("The age is NOT between 10 and 20 (it is over 20).")
            
    else:
        print("The age is NOT between 10 and 20 (it is under 10).")

except ValueError:
    print("Please enter a valid whole number.")

