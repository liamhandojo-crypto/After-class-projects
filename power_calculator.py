# take input
num=int(input("Enter your number: "))
power=int(input("Enter the exponent: "))

# find the power 
ans=1
for n in range(power):
    ans=ans*num

print(num,"to the power of",power,"is",ans)