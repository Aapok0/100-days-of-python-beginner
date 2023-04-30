from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""
    max_index = len(alphabet) - 1

    if direction == "encode":
        for character in text:
            if character in alphabet:
                index = alphabet.index(character)
                
                if index + shift > max_index:
                    new_index = index + shift - max_index - 1
                else:
                    new_index = index + shift
                cipher_text += alphabet[new_index]
            else:
                cipher_text += character
    elif direction == "decode":
        for character in text:
            if character in alphabet:
                index = alphabet.index(character)
                
                if index - shift < 0:
                    new_index = index - shift + max_index + 1
                else:
                    new_index = index - shift
                cipher_text += alphabet[new_index]
            else:
                cipher_text += character

    print(f"The {direction}d text is: {cipher_text}")

print(logo)
direction = input("Type 'encode' to encode, type 'decode' to decode or 'quit' to quit:\n")
quit = False

while quit == False:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
        direction = input("Do you want to continue? Type 'encode to encode, type 'decode' to decode or 'quit' to quit:\n")
    else:
        print(f"Unrecognized command '{direction}'.")
        direction = input("Type 'encode' to encode, type 'decode' to decode or 'quit' to quit:\n")

    if direction == "quit":
        quit = True