from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""
    max_index = len(alphabet) - 1

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

    if direction == "encode":
        for character in text:
            if character in alphabet:
                index = alphabet.index(character)
                
                if index + shift > max_index:
                    new_index = index + shift - max_index - 1
                else:
                    new_index = index + shift
                encoded_character = alphabet[new_index]
            else:
                encoded_character = character
            cipher_text += encoded_character
    elif direction == "decode":
        for character in text:
            if character in alphabet:
                index = alphabet.index(character)
                
                if index - shift < 0:
                    new_index = index - shift + max_index + 1
                else:
                    new_index = index - shift
                decoded_character = alphabet[new_index]
            else:
                decoded_character = character
            cipher_text += decoded_character

    print(f"The {direction}d text is: {cipher_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of characters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

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