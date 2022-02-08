alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
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

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)
