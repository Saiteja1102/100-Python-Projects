print("welcome to Rock Paper Scissor game")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

import random

player_input = input("Enter rock, paper or scissor : ")
player_input = player_input.lower()

print("------------------------------------------------------------")
print("You choosed ")
if player_input == "rock":
    player_input_number = 1
    print(rock)
elif player_input == "paper":
    player_input_number = 2
    print(paper)
elif player_input == "scissor":
    player_input_number = 3
    print(scissor)

# For random Number
random_number = random.randint(1,3)

print("Computer Chosen ")
if random_number == 1:
    bot = rock
    print(rock)
elif random_number == 2:
    bot = paper
    print(paper)
elif random_number == 3:
    bot = scissor
    print(scissor)

# Logic for the game
if player_input_number == random_number:
    print("Game Tie")
elif player_input_number == 1 and random_number == 2:
    print("You Lose!!")
elif player_input_number == 1 and random_number == 3:
    print("You Win!!")
elif player_input_number == 2 and random_number == 1:
    print("You Win!!")
elif player_input_number == 2 and random_number == 3:
    print("You Lose!!")
elif player_input_number == 3 and random_number == 1:
    print("You Lose!!")
elif player_input_number == 3 and random_number == 2:
    print("You Win!!")





