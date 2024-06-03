# Day 2
# Tip Calculator Project

print("Welcome to the Tip Calculator!!!")

total_bill = float(input("Enter your total bill : $"))
tip_percent = int(input("How much tip would u like to give(10, 12 or 15): "))
split_people = int(input("How many people to split the bill : "))

pay = ((total_bill*(tip_percent/100)+total_bill)/split_people)
# pay = round(pay,2)
pay = "{:.2f}".format(pay)

print(f"You should pay : ${pay}")