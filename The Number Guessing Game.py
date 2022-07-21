#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number beteween 1 and 100.")
difficulty_level = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
random_number = random.randint(1,100)
if difficulty_level == "hard":
    lives = 5
    print("You have 5 attemps remaing to guess the number.")
else:
    lives = 10
    print("You have 10 attempt remaining to guess the number.")

end_of_game = False

while not end_of_game:
    player_choice = int(input("make a guess: "))

    if player_choice > random_number:
        lives -= 1
        print(f"You guess too high. You have {lives} left")
        if lives == 0:
            end_of_game = True
            print(f"You ran out of live. Game Over. The number is {random_number}")
    elif player_choice < random_number:
        lives -= 1
        print(f"You guess too low. You have {lives} left")
        if lives == 0:
            end_of_game = True
            print(f"You ran out of live. Game Over. The number is {random_number}")
    else:
        end_of_game = True
        print("You guessed the correct number you win")




