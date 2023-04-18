# MSIT 501
# Aikerim Belispayeva
# project 2

print("Welcome to my Rock, Paper, Scissors Game!")

import random

min_games = 3
max_games = 11
player_choice = []
computer_choice = {"R": "Rock", "P": "Paper", "S": "Scissors"}
game_num = 0
valid_choices = ["R", "P", "S"]
player_score = 0
computer_score = 0
draws = 0
results = {}

while True:
    try:
        num_games = int(input("Enter a number of games to play -- odd number 3 to 11:"))
        if num_games < min_games or num_games > max_games:
            print("Sorry, out of range. Try again...")
            continue
        if num_games % 2 == 0:
            print("Please enter an odd number.")
            continue
        break
    except ValueError:
        print("Please, enter an integer value.")

game_num = 1
while game_num <= num_games:
    print("Game", game_num)
    current_winner = None
    try:
        computer_choice = str(random.choice(valid_choices))
        player_choice = input("Enter (R)ock, (P)aper, (S)cissors: ").upper()
        if player_choice == computer_choice:
            print("You Both Entered Same", "\nIt's a draw!")
            draws += 1
            current_winner = "Draw"
        elif player_choice == "R":
            print("Computer chose: ", computer_choice)
            if computer_choice == "P":
                print("Paper covers Rock", "\nComputer wins!")
                computer_score += 1
                current_winner = "Computer"
            else:
                print("Rock smashes Scissors", "\nYou win!")
                player_score += 1
                current_winner = "Player"
        elif player_choice == "P":
            print("Computer chose: ", computer_choice)
            if computer_choice == "S":
                print("Scissors cut Paper", "\nComputer wins!")
                computer_score += 1
                current_winner = "Computer"
            else:
                print("Paper covers Rock", "\nYou win!")
                player_score += 1
                current_winner = "Player"
        elif player_choice == "S":
            print("Computer chose: ", computer_choice)
            if computer_choice == "R":
                print("Rock smashes Scissors", "\nComputer wins!")
                computer_score += 1
                current_winner = "Computer"
            else:
                print("Scissors cut Paper", "\nYou win!")
                player_score += 1
                current_winner = "Player"
        else:
            print("Unknown Selection. Try again...")
            continue
        results[game_num] = (player_choice, computer_choice, current_winner)
        game_num += 1
    except ValueError:
        print("Invalid choice. Try again...")
        break

if computer_choice > player_choice:
    winner = "Computer"
else:
    "Player"

print()
print('Results for Games Played')
print('\n{:<10s}{:<10s}{:<10s}{:<10s}'.format("Game", "Player", "Computer", "Winner"))
print('-' * 40)
for key, value in results.items():
    print('{:<10d}{:<10s}{:<10s}{:<10s}'.format(key, value[0], value[1], value[2]))
print('-' * 40)
print('Player wins:', player_score)
print('Computer wins:', computer_score)
print('Draws:', draws)