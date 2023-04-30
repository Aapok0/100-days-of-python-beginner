alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(text, shift, direction):
    cipher_text = ""
    max_index = len(alphabet) - 1

    if direction == "encode":
        for letter in text:
            index = alphabet.index(letter)
            
            if index + shift > max_index:
                new_index = index + shift - max_index - 1
            else:
                new_index = index + shift
            encoded_letter = alphabet[new_index]
            cipher_text += encoded_letter

        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        for letter in text:
            index = alphabet.index(letter)
            
            if index - shift < 0:
                new_index = index - shift + max_index + 1
            else:
                new_index = index - shift
            decoded_letter = alphabet[new_index]
            cipher_text += decoded_letter

        print(f"The decoded text is {cipher_text}")

quit = False
direction = input("Type 'encode' to encode, type 'decode' to decode:\n")

while quit == False:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
        direction = input("Do you want to continue? Type 'encode to encode, type 'decode' to decode or 'quit' to quit:\n")
    else:
        print(f"Unrecognized command '{direction}'.")
        direction = input("Type 'encode' to encode, type 'decode' to decode or 'quit' to quit:\n")

    if direction == "quit":
        quit = True