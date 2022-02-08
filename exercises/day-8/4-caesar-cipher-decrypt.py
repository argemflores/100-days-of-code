alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    # initialize cipher text
    cipher_text = ''
    alphabet_length = len(alphabet)

    # shift every letter in the string
    for character in plain_text:
        # check if character is a letter in the alphabet
        if character in alphabet:
            # find the letter in the alphabet
            index = alphabet.index(character)

            # shift to new index
            new_index = index + shift_amount

            # new index is beyond list, so loop to the start (index: 0 letter: a)
            if new_index > alphabet_length - 1:
                new_index = new_index % alphabet_length

            # join new shifted letter to cipher text
            cipher_text += alphabet[new_index]
        else:
            # add character as is
            cipher_text += character

    # print cipher text
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

    # initialize cipher text
    plain_text = ''
    alphabet_length = len(alphabet)

    # shift every letter in the string
    for character in cipher_text:
        # check if character is a letter in the alphabet
        if character in alphabet:
            # find the letter in the alphabet
            index = alphabet.index(character)

            # shift to new index
            new_index = index - shift_amount

            # new index is beyond list, so loop to the end (index: 25 letter: z)
            if new_index < 0:
                new_index = new_index + alphabet_length

            # join new shifted letter to plain text
            plain_text += alphabet[new_index]
        else:
            # add character as is
            plain_text += character

    # print plain text
    print(f"The encoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction.lower() == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction.lower() == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
