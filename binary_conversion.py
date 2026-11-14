#take user input
num=float(input("Enter your number: "))
whole=int(num)
decimal=num-whole

#calculate the binary of whole
binary_whole=""
while whole>0:
    binary_whole=str(whole%2)+binary_whole
    whole=whole//2

#calculate the binary of decimal
binary_decimal=""
for i in range(5):
    decimal=decimal*2
    for j in range(1):
        binary_decimal=binary_decimal+str(int(decimal))
    decimal=decimal-int(decimal)

#print the binary number
print("The binary number of",num,"is",binary_whole+"."+binary_decimal)