print("select your ride")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice : "))

if (choice == 1):
    print("what type of bike")
    print("1. Sports Bike")
    print("2. Cruiser Bike")

    choice1 = int(input("Enter you choice2 : "))
    if (choice1 == 1):
        print("You have selected Sports Bike")
    else:
        print("You have selected Cruiser Bike")

elif (choice == 2):
    print("what type of car")
    print("1. Sedan")
    print("2. SUV")

    choice2 = int(input("Enter you choice2 : "))
    if (choice2 == 1):
        print("You have selected Sedan")
    else:
        print("You have selected SUV")
else:
    print("Invalid choice")
    
   