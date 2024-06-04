print("Welcome to python pizza")
size = input("What pizza size do u want? S, M or L : ")
add_peperoni = input("Do u want to add peperoni? Y or N : ")
extra_cheese = input("Do u want to add Extra cheese? Y or N : ")

price = 0
if size == "S":
    price += 15
    if add_peperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
elif size == "M":
    price += 20
    if add_peperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
elif size == "L":
    price += 25
    if add_peperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1

print("Thank you for choosing Python pizza Deliveries!!")
print(f"Your final bill is ${price}")