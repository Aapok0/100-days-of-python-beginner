import random
from hangman_art import *
from hangman_words import word_list

print(logo, '\n')
print("Try to guess the following blank word letter by letter. Wrong answers take hangman closer to hanging. Don't let that happen..")

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display += '_'

lives = len(stages) - 1
guesses = []

while '_' in display:
    print(chosen_word)
    print(f'\n{" ".join(display)}')
    print(stages[lives])

    guess = input('Guess a letter: ').lower()
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
        if lives == 0:
            print(f'You guessed wrong. Letter {guess} is not in the word.')
            print(f'\n{" ".join(display)}')
            print(stages[lives])
            print('You let hangman be hung.. You lose!')
            break
        else:
            print(f'You guessed wrong. Letter {guess} is not in the word. Hangman is one step closer to hanging..')
    else:
        print(f'Correct! Letter {guess} is found in the word.')

    if '_' not in display:
        print(f'\n{" ".join(display)}')
        print(stages[lives])
        print('Congratulations, you found the word and saved hangman! You win!')
