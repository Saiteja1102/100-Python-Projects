import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to pyPassword Generator")
number_letters = int(input("How many letters would you like in your password : "))
number_symbols = int(input("How many symbols would you like : "))
number_numbers = int(input("How many numbers would you like : "))


# Easy One
# password = ""
# for i_letters in range(0,number_letters):
#     rand_letters = random.randint(0,len(letters)-1)
#     password = password + letters[rand_letters]

# for i_symbols in range(0,number_symbols):
#     rand_symbols = random.randint(0,len(symbols)-1)
#     password = password + symbols[rand_symbols]

# for i_numbers in range(0,number_numbers):
#     rand_numbers = random.randint(0,len(numbers)-1)
#     password = password + numbers[rand_numbers]

# print(password)

# Hard Level
password_list = []
for i_letters in range(0,number_letters):
    rand_letters = random.choice(letters)
    password_list.append(rand_letters)

for i_symbols in range(0,number_symbols):
    rand_symbols = random.choice(symbols)
    password_list.append(rand_symbols)

for i_numbers in range(0,number_numbers):
    rand_numbers = random.choice(numbers)
    password_list.append(rand_numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)
# print("".join(password_list))

for i in password_list:
    print(i,end="")

print("")