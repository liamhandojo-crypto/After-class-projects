#define the functions
def rectangle(A,B):
    return (A+B)*2
def circum(A):
    return 2*3.14*A

#take user input for choice
print("Python Perimeter and Circumference Calculator!")
print("Please select either rectangle or circle.")
print("a. Perimeter of a rectangle")
print("b. Circumference of a circle")

choice=input("Enter your choice: ")

#if elif statement
if choice=="a":
    length=int(input("Enter the length of the rectangle in cm: "))
    breadth=int(input("Enter the breadth of the rectangle in cm: "))
    print("The perimeter of the rectangle is",rectangle(length,breadth))
elif choice=="b":
    radius=int(input("Enter the radius of the circle in cm: "))
    print("The circumference of the circle is",circum(radius))
else:
    print("The option you have entered does not exist.")

#thank you message
print("Thank you for using the Python Perimeter and Circumference Calculator!")