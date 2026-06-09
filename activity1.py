# Take input for the student that thee student can atend then exam
medical_cause = input("Did you have a medical cause ? (Y/N) :  ").strip().upper()

#checking the user input preticting the output accordingly
if medical_cause == "Y":
    print("You allowed")
else:
    #take input out og the attendence
    attendence = int(input("Enter the attendence of the student : "))
 
    if attendence >= 75:
        print("You allowed")

    else:
        print("You are not allowed")
     
