rock = '''
    ROCK
   _______
  /       \\
 |  O O O  |
 |  O O O  |
 |  O O O  |
  \\_______/
'''

paper = '''
    PAPER
   _______
  /       \\
 |         |
 |         |
 |         |
  \\_______/
'''

scissors = '''
  SCISSORS
   _______
  /       \\
 |    /\   |
 |   /  \\  |
 |  /    \\ |
  \\_______/
'''

# Example: Print each symbol
print("Welcome to rock Paper and Sissors")
print(rock)
print(paper)
print(scissors)
import random
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please choose again (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}\n")

if __name__ == "__main__":
    play_game()

