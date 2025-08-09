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
user_choice = int(input("What do you choose? Type '0' for ROCK, '1' for PAPER or '2' for SCISSORS\n"))
computer_choice = random.randint(0 , 2)

game = [rock, paper, scissors]

if user_choice > 2:
    print("You have entered a wrong invalid input!! You loose!!")
else:
    print(f"You Choose: {game[user_choice]}")
    print(f"Computer Chose: {game[computer_choice]}")

    if user_choice == 0 and computer_choice == 1:
        print("You Lose!!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose!!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!!")
    elif user_choice == computer_choice:
        print("It's a Tie!!")
    else:
        print("You Win!!")