line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1,line2,line3]
print("Hiding your treasure, X marks the spot.")
position = input("Enter the position Like B1 or A2 or C0: ")
first = position[0]
if first == "A" or first == "a":
    first_position = 0
elif first == "B" or first == "b":
    first_position = 1
elif first == "C" or first == "c":
    first_position = 2
second_position  = int(position[1])

if second_position == 0:
    line1[first_position] = "X"
elif second_position == 1:
    line2[first_position] = "X"
elif second_position == 2:
    line3[first_position] = "X"

     
print(f"{line1}")
print(f"{line2}")
print(f"{line3}")