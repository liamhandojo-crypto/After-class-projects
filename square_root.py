# take user input
number = int(input("Please enter a whole number: "))

# find the square root of the user's number
root = number**0.5

# check if the square root is a whole number
if root == int(root):
    print("The square root of", number, "is", root)
else:
    print("This number does not have a square root that is a whole number.")