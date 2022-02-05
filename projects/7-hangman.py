# Hangman 🏗
# https://replit.com/@ArgemFlores/hangman

# import libraries
import random
import hangman_words
import hangman_art
from replit import clear

# choose a random word from the imported word list
chosen_word = random.choice(hangman_words.word_list)

# set game flags
end_of_game = False
lives = 6

# print welcome messages
print(hangman_art.logo)
print('Welcome to Hangman! 🏗')

# create blanks and print display and lives
display = ['_'] * len(chosen_word)
print(f"\n{' '.join(display)}")
print(hangman_art.stages[lives])

# start game and loop until end of game
while not end_of_game:
    # ask user to type a letter
    guess = input("Guess a letter: ").lower()

    # clear previous screen
    clear()

    print(hangman_art.logo)

    # notify that letter is already guessed
    if guess in display:
        print(f"🤨 '{guess}' is already guessed. Try again.")
    elif guess in chosen_word and '_' in display:
        print(" ")

    # check guessed letter from the chosen word
    for i, letter in enumerate(chosen_word):
        # replace display with correct letter
        if letter == guess:
            display[i] = letter

    # notify if guess is not in the word
    if guess not in chosen_word:
        # lose one life
        lives -= 1

        # end game and user lost if life reaches 0
        if lives == 0:
            end_of_game = True
            print(f"😵 You lose... The word is '{chosen_word}'. Sorry... 🪦")
        else:
            # show current lives
            print(f"😰 '{guess}' is not in the word. {lives} chance/s left.")

    # end game and user wins if all letters are guessed
    if "_" not in display:
        end_of_game = True
        print(f"🥳 You win! The word is '{chosen_word}'. Congratulations! 🎉")

    # print displayed word
    print(f"\n{' '.join(display)}")

    # print hangman stages
    print(hangman_art.stages[lives])
