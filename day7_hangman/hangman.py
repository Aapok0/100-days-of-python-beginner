import random

#Step 5

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

from hangman_art import *
from hangman_words import word_list

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game

print(logo, '\n')
print("Try to guess the following blank word letter by letter. Wrong answers progress hangman's work. Don't let hangman finish his job..\n")

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display += '_'
print(f'{" ".join(display)}\n')

lives = len(stages) - 1
guesses = []

while '_' in display:
    guess = input('Guess a letter: ').lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in guesses:
        print(f'You already guessed {guess}.')
        continue
    guesses += guess

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            correct_guess = True
    if guess not in chosen_word:
        lives -= 1

    print(f'{" ".join(display)}\n')

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.

    print(stages[lives])

    if lives == 0:
        print('You lose!')
        break
    if '_' not in display:
        print('Congratulations, you win!')
