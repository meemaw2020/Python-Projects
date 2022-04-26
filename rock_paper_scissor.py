import random

options = ['rock', 'paper', 'scissor']

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    ran_num = random.randint(0,2)
    computer_input = options[ran_num]
    print("The program picks", computer_input, ".")

    if user_input == "rock" and computer_input == "scissor":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissor" and computer_input == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == computer_input:
        print("Draw!")
    
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, " times.")
print("The program won", computer_wins, " times.")