# find out the temperature and rain from user input
temperature=int(input("Enter the temperature outside: "))
rain_input=input("Is it raining? Answer with yes or no: ")

rain=False
if rain_input == "yes":
    rain=True

# decide what clothes Rohan can wear
if temperature >20 and temperature <30 and not rain:
    print("It is warm outside. Wear a T-shirt and shorts.")
else:
    if temperature >=30 and not rain:
        print("It is hot outside. Wear a singlet and wear a cap.")
    else:
        if temperature >=30 and rain:
            print("Wear a T-shirt and bring an umbrella.")
        else:
            if temperature >=15 and temperature <=20:
                print("Wear a jacket.")
            else:
                if temperature <15:
                    print("It is cold outside. Wear a thick jacket.")
