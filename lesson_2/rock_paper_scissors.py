import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}.")

    if ((player == "rock" and 
         (computer == "scissors" or computer == "lizard")) or
        (player == "paper" and 
         (computer == "rock" or computer == "spock")) or
        (player == "scissors" and 
         (computer == "paper" or computer == "lizard")) or
        (player == "spock" and 
         (computer == "rock" or computer == "scissors")) or
        (player == "lizard" and 
         (computer == "paper" or computer == "spock"))):
        prompt("You win!")
    elif ((computer == "rock" and 
         (player == "scissors" or player == "lizard")) or
        (computer == "paper" and 
         (player == "rock" or player == "spock")) or
        (computer == "scissors" and 
         (player == "paper" or player == "lizard")) or
        (computer == "spock" and 
         (player == "rock" or player == "scissors")) or
        (computer == "lizard" and 
         (player == "paper" or player == "spock"))):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)
    
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if answer[0] == 'n':
        break