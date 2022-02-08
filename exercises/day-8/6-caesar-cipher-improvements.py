alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encrypt or decrypt a message
def caesar(text, shift, direction):
    # initialize new text and get alphabet list length
    new_text = ''
    alphabet_length = len(alphabet)

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
    print(f"The {direction}d text is {new_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

choice = 'yes'

while choice != 'no':
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    choice = input("\nDo you want to restart? Type 'yes' to repeat or 'no' to exit:\n")
