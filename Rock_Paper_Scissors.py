import random

def play():
    player = input('Your choice: "R" - rock, "P" - Paper, "S" - Scissors: ').upper()
    print(player)
    computer = random.choice(['R', 'P', 'S'])
    print(computer)

    if player == computer:
        return 'It\'s draw'
    if is_win(player,computer):
        return "You win"
    
    return "You lost"


def is_win(player,computer):
    if (player == 'R' and computer == 'S') or (player == 'S' and computer == 'P') or (player == 'P' and computer == 'R'):
        return True

print(play())
