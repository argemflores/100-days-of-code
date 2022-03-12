# Caesar Cipher 🔏
# https://replit.com/@ArgemFlores/caesar-cipher

import string
import art

"""Encrypt or decrypt a message"""
def caesar(text, shift, direction):
    # initialize alphabet and new text
    alphabet = string.ascii_lowercase
    alphabet_length = len(alphabet)
    new_text = ''

    # shift every letter in the string
    for character in text:
        # check if character is a letter in the alphabet
        if character in alphabet:
            # find the letter in the alphabet
            index = alphabet.index(character)

            if direction == 'encode':
                # shift to new index
                new_index = index + shift

                # new index is beyond list, so loop to the start (index: 0 letter: a)
                if new_index > alphabet_length - 1:
                    new_index = new_index % alphabet_length
            elif direction == 'decode':
                # shift to new index
                new_index = index - shift

                # new index is beyond list, so loop to the end (index: 25 letter: z)
                if new_index < 0:
                    new_index = new_index + alphabet_length

            # join new shifted letter to new text
            new_text += alphabet[new_index]
        else:
            # add character as is
            new_text += character

    # print new text
    print(f"\n🔡 The {direction}d text is '{new_text}'.")

if __name__ == '__main__':
    # print the caesar cipher log
    print(art.logo)
    print('Welcome to Caesar Cipher! 🔏')

    choice = 'yes'

    # start the program
    while choice == 'yes':
        # ask direction
        direction = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n")

        # invalid direction
        if direction.lower() not in ['encode', 'decode']:
            print('Invalid action! Try again.')
            continue

        # type message and shift
        text = input("Type your message:\n").lower()
        shift = input("Type the shift number (1 to N):\n")

        if shift.isnumeric():
            # convert shift to integer
            shift = int(shift)
        else:
            # invalid shift (not a number)
            print('Invalid shift! Try again.')
            continue

        # process message based on given direction
        caesar(text=text, shift=shift, direction=direction)

        # ask to restart or exit the program
        choice = input("\nDo you want to restart? Type 'yes' to repeat or 'no' to exit:\n")

    print('\n🔏 Thanks for using Caesar Cipher! 😄')
