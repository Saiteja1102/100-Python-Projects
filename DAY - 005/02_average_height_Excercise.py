heights_value = input("Enter the heights using space seperated values : ")
heights_list = heights_value.split(" ")

# For converting to integers
for i in range(0,len(heights_list)):
    heights_list[i] = int(heights_list[i])
    
# total height
total_height = 0
for t_height in heights_list:
    total_height += t_height
print("Total height = ", total_height)

# Length of the list
number_of_height = 0
for n_height in heights_list:
    number_of_height += 1
print("Number of students = ", number_of_height)

# Average of heights
average_height = int(total_height/number_of_height)
print("Average height = ",average_height)