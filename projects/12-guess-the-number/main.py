# Number Guessing Game
# https://replit.com/@ArgemFlores/guess-the-number

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# import libraries
import art
from random import randint

# print logo and welcome message
print(art.logo)
message = """š¤ Guess the mystery number! What could it be?
   Clue: It is somewhere between 1 and 100!\n"""
print(message)

# ask difficulty level
levels = {'easy': 10, 'hard': 5}
chosen_level = ''

# loop until correct level is chosen
while True:
    # ask level
    chosen_level = input(f"š  Choose your level ('easy' 10 tries; 'hard' 5 tries): ").strip().lower()

    # level is invalid, try again
    if chosen_level not in levels.keys():
        print(f"š '{chosen_level}' is invalid. Try again!\n")
    else:
        # level is valid, break out of loop
        break

# get the number of tries based on the chosen level
tries = levels[chosen_level]
print(f"   You have {tries} tries to guess the mystery number. Let's go!")

# pick the mystery number
mystery_number = randint(1, 100)

# loop until guess is correct or tries ran out
while tries > 0:
    # ask guess
    guess = input("\nš¤ Type your guess: ")

    # guess is not a number or out of bounds
    if not guess.isnumeric() or int(guess) < 1 or int(guess) > 100:
        print(f"ā  '{guess}' is invalid. Try again!")
        continue

    # typecast guess to integer
    guess = int(guess)

    # guess is correct, congratulate and end game
    if guess == mystery_number:
        print(f"\nā You got it! Congratulations! š„³")
        print(f"   The mystery number is {mystery_number}! š®")
        print(f"   Thanks for playing! š")
        break
    else:
        # guess is too low
        if guess < mystery_number:
            print(f"ā {guess} is too LOW! ā¬ļø")
        else:
            # guess is too high
            print(f"ā {guess} is too HIGH! ā¬ļø")

        # reduce tries by 1
        tries -= 1

        # show number of tries left
        if tries > 0:
            print(f"   You have {tries} tries left.")
else:
    # tries ran out, end game
    print(f"\nā Oops, you ran out of tries... ā¹ļø")
    print(f"   The mystery number is {mystery_number}. š®")
    print(f"   Thanks for playing! š")
