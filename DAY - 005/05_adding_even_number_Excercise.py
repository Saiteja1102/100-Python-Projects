# Even number sum calculator

till_number = int(input("Enter the number till you want to add : "))
even_sum = 0
for i in range(0,till_number+1,2):
    even_sum += i

print("The even sum is = ",even_sum)