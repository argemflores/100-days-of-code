alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
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

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction.lower() == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
