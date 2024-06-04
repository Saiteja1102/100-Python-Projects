print("Welcome to the rollercoster!!!")
height = int(input("Enter your height in cm :  "))

if height > 120:
    print("You can ride the rollercoster!!")
else:
    print("Sorry, You can't ride the rollercoster....")


# 2
water_level = int(input("Enter the current water level : "))

if water_level > 80:
    print("Drain water..")
else:
    print("continue filling..")