print("Welcome to the rollercoster!!")
height = int(input("Enter your height in cm : "))

if height >= 120:
    print("You can ride..")
    age = int(input("Enter your age : "))
    if age < 12:
        print("Pay $7")
    elif age < 18:
        print("Pay $12")
    else:
        print("Pay $20")
else:
    print("Sorry, You are not allowed to ride..")