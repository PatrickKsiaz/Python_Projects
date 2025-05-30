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

import random

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Get user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Validate input
if user_choice < 0 or user_choice > 2:
    print("Invalid number! You lose.")
else:
    print(f"You chose: {choices[user_choice]}")

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")


