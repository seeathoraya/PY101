import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f"==> {message}")

def convert_choice(string):
    match string:
        case 'r':
            return 'rock'
        case 'p':
            return 'paper'
        case 'sc':
            return 'scissors'
        case 'sp':
            return 'spock'
        case 'l':
            return 'lizard'

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}.")
    if player_wins(player, computer):
        prompt("You win!")
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")

def start_match():
    player_score = 0
    computer_score = 0

    while (player_score < 3 and computer_score < 3):
        prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = convert_choice(input())

        while choice not in (VALID_CHOICES):
            prompt("That's not a valid choice")
            choice = convert_choice(input())

        computer_choice = random.choice(VALID_CHOICES)

        display_winner(choice, computer_choice)

        if player_wins(choice, computer_choice):
            player_score += 1
        elif choice != computer_choice:
            computer_score += 1

        prompt(f"Player: {player_score} wins")
        prompt(f"Computer: {computer_score} wins")
        print()

        if player_score == 3:
            prompt("Game over. You won the match!")
        elif computer_score == 3:
            prompt("Game over. Computer won the match!")
        else:
            continue


while True:
    start_match()

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer.startswith('n'):
        break