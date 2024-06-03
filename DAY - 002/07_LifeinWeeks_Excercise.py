# You have 90 years total
age = int(input("Enter your age : "))
total_weeks = 90*52
total_age_weeks = age*52
total_left_weeks = total_weeks - total_age_weeks
print(f"You have {total_left_weeks} weeks left.")