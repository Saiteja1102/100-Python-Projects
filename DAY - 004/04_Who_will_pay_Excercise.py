import random
enter_names = input("Enter the names by comma seperated values : ")
names = enter_names.split(",")

length = len(names)
random_name_number = random.randint(0,length-1)

print(f"{names[random_name_number]} is going to buy the meal today!!")