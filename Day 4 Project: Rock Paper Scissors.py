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
import random
random_integer = random.randint(0,2)
choice = int(input("Hello, welcome the Rock, Paper, Scissors game. Please enter 0 for Rock, 1 for Paper, and 2 for Scissors:\n " ))
#Generate random numbers between 0 and the last index.
if choice == 0 and random_integer == 0:
    print(f"you chose {rock} and the computer chose {rock}\n The game is a draw")
elif  choice == 0 and random_integer == 1:
    print(f"you chose {rock} and the computer chose {paper}\n You lose")
elif choice == 0 and random_integer == 2:
    print(f"you chose {rock} and the computer chose {scissors}\n You WIN")
elif choice == 1 and random_integer == 0:
    print(f"You choose {paper} and the computer choose {rock}\n You WIN")
elif choice == 1 and random_integer == 1:
    print(f"you chose {paper} and the computer chose {paper}\n The game is a draw")
elif choice == 1 and random_integer == 2:
    print(f"you chose {paper} and the computer chose {scissors}\n You LOSE")
elif choice == 2 and random_integer == 0:
    print(f"You choose {scissors} and the computer choose {rock}\n You LOSE")
elif choice == 2 and random_integer == 1:
    print(f"You choose {scissors} and the computer choose {paper}\n Your WIN")
else:
    print(f"You choose {scissors} and the computer choose {scissors}\n The game is a draw")
