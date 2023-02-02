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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
value_map = {0: rock, 1: paper, 2: scissors}
computer_choice = random.randint(0, 2)
print(value_map[user_choice])
print(f"Computer chose \n{value_map[computer_choice]}")
if user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == computer_choice:
    print("It's a Draw")
else:
    print("You lose")
