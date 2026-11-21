#take user input
row=int(input("Enter the number of rows: "))

#make the pattern using nested loop
for i in range(1,row+1):
    for n in range(row-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()