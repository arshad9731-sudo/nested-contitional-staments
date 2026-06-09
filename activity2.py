# Take input from the user consumed from the user
units = int(input("Enter the number of units consumed : "))
#check conditions of units consumed
# Then calculate the amount and the surcharege accordingly
# Surcharge it the tax value

# Check for units less then 50
if (units < 50):
    amount = units * 0.25
    surcharge = amount * 25

elif (units <= 100):
    amount = 130 +((units - 50 ) * 3.25)
    surcharge = amount * 35

elif (units <= 200):
    amount = 130 + 162.5 + ((units - 100) * 5.25)
    surcharge = amount * 45

else:
    amount = 130 + 162.5 + 525 + ((units - 200) * 7.25)
    surcharge = amount * 50
total = amount + surcharge
print("/nELECTRICITY BILL = %.2f" % total)
print("Surcharge = %.2f" % surcharge)
