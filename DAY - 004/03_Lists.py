# List --> Data Structure

states_of_india = ["Telangana","Punjab","Andrapradesh","Tamil Nadu","Kerala","Karnataka",
                   "Madhya Pradesh","Maharashtra","west bengal","Uttarpradesh","Odisha"]

print(states_of_india[0])
print(states_of_india[1])
print(states_of_india[2])
print(states_of_india[3])

print(states_of_india[-1])
print(states_of_india[-2])
print(states_of_india[-3])
print(states_of_india[-4])

states_of_india[2] = "Andhra"
states_of_india.append("Jammu and Kashmir")
states_of_india.extend(["Haryana","Bihar","Rajasthan"])

print(states_of_india)