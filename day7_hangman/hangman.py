import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display += '_'
print(f'{" ".join(display)}\n')

#Step 4

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = len(stages) - 1

while '_' in display:
    guess = input('Guess a letter: ').lower()

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            correct_guess = True
    if guess not in chosen_word:
        lives -= 1

    print(f'{" ".join(display)}\n')

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])

    if lives == 0:
        print('You lose!')
        break
    if '_' not in display:
        print('Congratulations, you win!')
