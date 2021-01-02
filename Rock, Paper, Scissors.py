import random


def play():
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a Tie!"
    if winner(user, computer):
        return 'You Win!'
    else:
        return 'You Lose!'


def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
            or (player == 's' and opponent == 'p'):
        return True


print(play())
