import random

# ASCII-art gotten from starting code of the course
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hands = [rock, paper, scissors]

player_rock = ["It's a draw.", "Haha, you lose!", "Oh... you win..."]
player_paper = ["Oh... you win...", "It's a draw.", "Haha, you lose!"]
player_scissors = ["Haha, you lose!", "Oh... you win...", "It's a draw."]
result_map = [player_rock, player_paper, player_scissors]

print("Hi! Try to beat me in Rock Paper Scissors! \n")
player_choice = input('Make your choice: "0" for rock, "1" for paper or "2" for scissors: \n')

if player_choice == "0" or player_choice == "1" or player_choice == "2":
    player_choice_int = int(player_choice)
    print("\nPlayer:" + hands[player_choice_int])

    computer_choice = random.randint(0, 2)
    print("Computer:" + hands[computer_choice])

    print(result_map[player_choice_int][computer_choice])
else:
    print('\nInvalid choice. Next time remember to type "0" for rock, "1" for paper or "2" for scissors.')