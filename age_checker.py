# find out the user's name and age
name=input("Enter your name: ")
age=int(input("Enter your age: "))

# decide if the user can enrol in Mr Raj's class
if age<10 or age>20:
    print("You may not enrol in Mr Raj's class due to your age.")

elif age<=10 or age<=20:
    print("Thank you for choosing Mr Raj as your teacher!")
    print("Choose which subject you wish to take\n")
    print("Enter 1 for Math")
    print("Enter 2 for English")
    print("Enter 3 for Science")
    print("Enter 4 for History")
    subject=int(input("Enter your choice: "))
    if subject==1:
        choice='Math'
        print("You have chosen Math!")
    elif subject==2:
        choice='English'
        print("You have chosen English!")
    elif subject==3:
        choice='Science'
        print("You have chosen Science!")
    elif subject==4:
        choice='History'
        print("You have chosen History!")
    else:
        print("That choice is not available.")

    print(name,",thank you for enrolling in Mr Raj's",choice,"class!")



