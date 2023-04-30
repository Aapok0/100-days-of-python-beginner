alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text, shift):
    encoded_text = ""
    max_index = len(alphabet) - 1

    for letter in text:
        index = alphabet.index(letter)
        
        if index + shift > max_index:
            new_index = index + shift - max_index - 1
        else:
            new_index = index + shift
        encoded_letter = alphabet[new_index]
        encoded_text += encoded_letter
    
    print(f"The encoded text is {encoded_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decode(text, shift):

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decoded text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

    decoded_text = ""
    max_index = len(alphabet) - 1

    for letter in text:
        index = alphabet.index(letter)
        
        if index - shift < 0:
            new_index = index - shift + max_index + 1
        else:
            new_index = index - shift
        decoded_letter = alphabet[new_index]
        decoded_text += decoded_letter
    
    print(f"The decoded text is {decoded_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

quit = False
direction = input("Type 'encode' to encode, type 'decode' to decode:\n")

while quit == False:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode(text, shift)
        direction = input("Do you want to continue? Type 'encode to encode, type 'decode' to decode or 'quit' to quit:\n")
    elif direction == "decode":
        decode(text, shift)
        direction = input("Do you want to continue? Type 'encode to encode, type 'decode' to decode or 'quit' to quit:\n")
    else:
        print(f"Unrecognized command '{direction}'.")
        direction = input("Type 'encode' to encode, type 'decode' to decode:\n")

    if direction == "quit":
        quit = True