import random

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']

while True:
    player_move = input("Your move: ")

    if player_move == 'q':
        break

    computer_move = random.choice(moves)

    # For debug only
    print("User: " + player_move)
    print("Computer: " + computer_move)

    if player_move == computer_move:
        print("Tie!")
    elif player_move + computer_move in player_wins:
        print("User Wins!")
    else:
        print("Computer Wins!")
