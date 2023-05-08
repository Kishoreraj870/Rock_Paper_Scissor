import random
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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game[user_input])

computer_rand = random.randint(0,2)
print("computer choose:")
print(game[computer_rand])

if user_input<0 and user_input>=3:
  print("invalid input please try again")
elif user_input == 0 and computer_rand == 2:
  print("you win")
elif computer_rand == 2 and user_input == 0:
  print("you lose")
elif user_input>computer_rand:
  print("you win")
elif user_input<computer_rand:
  print("you lose")
elif user_input==computer_rand:
  print("draw")
  