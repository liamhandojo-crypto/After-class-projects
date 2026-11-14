#take user input
num=int(input("Enter your number: "))
temp=num
reverse=0

#use while loop to reverse the num
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10

print("The reverse number of",num,"is",reverse)

