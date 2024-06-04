print("Welcome to the rollercoster!!")
height = int(input("Enter your height in cm : "))

if height >= 120:
    print("You can ride..")
    age = int(input("Enter your age : "))
    bill = 0
    if age < 12:
        bill = 7
        print("Pay $7")
    elif age < 18:
        bill = 12
        print("Pay $12")
    else:
        bill = 20
        print("Pay $20")

    want_photo = input("Do you want a photo taken? Y or N : ")
    if want_photo == "Y":
        bill += 3
    
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, You are not allowed to ride..")