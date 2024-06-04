print("Love Calculator")
name1 = input("Enter name 1 : ")
name2 = input("Enter name 2 : ")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_count = lower_name1.count("t")
r_count = lower_name1.count("r")
u_count = lower_name1.count("u")
e_count = lower_name1.count("e")

t_count2 = lower_name2.count("t")
r_count2 = lower_name2.count("r")
u_count2 = lower_name2.count("u")
e_count2 = lower_name2.count("e")

first_digit = t_count+t_count2+r_count+r_count2+u_count+u_count2+e_count+e_count2

l_count = lower_name1.count("l")
o_count = lower_name1.count("o")
v_count = lower_name1.count("v")
e_count_l = lower_name1.count("e")

l_count2 = lower_name2.count("l")
o_count2 = lower_name2.count("o")
v_count2 = lower_name2.count("v")
e_count2_l = lower_name2.count("e")

second_digit = l_count+o_count+v_count+e_count_l+e_count2_l+l_count2+o_count2+v_count2

score = int(str(first_digit) + str(second_digit))

print("The Love calculator is calculating.....")
if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")




