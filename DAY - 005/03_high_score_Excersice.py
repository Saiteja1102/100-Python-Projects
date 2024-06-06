scores = input("Enter the scores by space sperated : ")
scores_list = scores.split(" ")

# For convertering to integers
for i in range(0,len(scores_list)):
    scores_list[i] = int(scores_list[i])

# Finding highest number
highest_number = 0
for i in range(1,len(scores_list)):
    if highest_number < scores_list[i-1]:
        if scores_list[i-1] > scores_list[i]:
            highest_number = scores_list[i-1]
        else:
            highest_number = scores_list[i]

print(f"The highest score in the class is {highest_number}")