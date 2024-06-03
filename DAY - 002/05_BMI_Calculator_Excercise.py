# BMI Calculator
# BMI = Weight(kg)/height^2(m^2)

# 1st input : Enter height in meters
height = float(input("Enter height in meters : "))

# 2nd input : Enter weight in kilograms
weight = int(input("Enter weight in kilograms : "))

bmi = int(weight/height**2)
print("BMI is : ",bmi)