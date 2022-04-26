import random

options = ['rock', 'paper', 'scissor']
user_wins = 0
computer_wins = 0
username = input('Player Name >> ')
money = 1000
borrow_money = 0

print("Welcome to the game,", username, ".Your starting amount is", money, "dollars.")

def program_win():
    global user_wins
    global computer_wins
    global money
    global borrow_money
    while True:
        if money < 1:
            print("You lost but you can borrow money from me up to 1000 dollars.")
            borrow = input("Will you borrow? yes/no").lower()
            if borrow == "yes":
                borrow_amount = input("Type the amount: ")
                money += int(borrow_amount)
                borrow_money += int(borrow_amount)
                print("You now have ", money, " dollars to play")
                borrow_not_valid = int(borrow_amount) > 1000 or int(borrow_amount) < 1
                while borrow_not_valid:
                    print("Please enter a valid amount.")
                    borrow_amount = input("Type the amount: ")
                    borrow_not_valid = int(borrow_amount) > 1000 or int(borrow_amount) < 1
            if borrow == "no":
                break

        bet = input("Place your bet >> ")
        bet_not_valid = int(bet) > money or int(bet) < 0
        while bet_not_valid:
            print("Please enter a valid bet.")
            bet = input("Place valid bet >> ")
            bet_not_valid = int(bet) > money or int(bet) < 0

        bet = int(bet)

        user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        if user_input == "rock":
            rock_options = options
            if len(rock_options) < 6:
                rock_options.append("paper")
                rock_options.append("paper")
                rock_options.append("rock")
            ran_num = random.randint(0,5)
            computer_input = rock_options[ran_num]
            print("The program picks", computer_input, ".")
            del rock_options[3]
            del rock_options[3]
            del rock_options[3]
        
        elif user_input == "paper":
            paper_options = options
            if len(paper_options)  < 6:
                paper_options.append("scissor")
                paper_options.append("scissor")
                paper_options.append("paper")
            ran_num = random.randint(0,5)
            computer_input = paper_options[ran_num]
            print("The program picks", computer_input, ".")
            del paper_options[3]
            del paper_options[3]
            del paper_options[3]    

        elif user_input == "scissor":
            scissor_options = options
            if len(scissor_options) < 6:
                scissor_options.append("scissor")
                scissor_options.append("rock")
                scissor_options.append("rock")
            ran_num = random.randint(0,5)
            computer_input = scissor_options[ran_num]
            print("The program picks", computer_input, ".")
            del scissor_options[3]
            del scissor_options[3]
            del scissor_options[3]    

        if user_input == "rock" and computer_input == "scissor":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")

        elif user_input == "paper" and computer_input == "rock":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")
        
        elif user_input == "scissor" and computer_input == "paper":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")
        
        elif user_input == computer_input:
            print("Draw!")
            print("You have", money, " dollars now.")
        
        else:
            print("You lost!")
            computer_wins += 1
            money -= bet
            print("You have", money, " dollars now.")

def user_win():
    global user_wins
    global computer_wins
    global money
    global borrow_money
    while True:
        if money > 1500:
            program_win()
            break

        if money < 1:
            print("You lost but you can borrow money from me up to 1000 dollars.")
            borrow = input("Will you borrow? yes/no").lower()
            if borrow == "yes":
                borrow_amount = input("Type the amount: ")
                money += int(borrow_amount)
                borrow_money += int(borrow_amount)
                print("You now have ", money, " dollars to play")
                borrow_not_valid = int(borrow_amount) > 1000 or int(borrow_amount) < 1
                while borrow_not_valid:
                    print("Please enter a valid amount.")
                    borrow_amount = input("Type the amount: ")
                    borrow_not_valid = int(borrow_amount) > 1000 or int(borrow_amount) < 1

            if borrow == "no":
                break

        bet = input("Place your bet >> ")
        bet_not_valid = int(bet) > money or int(bet) < 0
        while bet_not_valid:
            print("Please enter a valid bet.")
            bet = input("Place valid bet >> ")
            bet_not_valid = int(bet) > money or int(bet) < 0

        bet = int(bet)

        user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        if user_input == "rock":
            rock_options = options
            if len(rock_options) < 6:
                rock_options.append("scissor")
                rock_options.append("scissor")
                rock_options.append("rock")
            ran_num = random.randint(0,5)
            computer_input = rock_options[ran_num]
            print("The program picks", computer_input, ".")
            del rock_options[3]
            del rock_options[3]
            del rock_options[3]
        
        elif user_input == "paper":
            paper_options = options
            if len(paper_options)  < 6:
                paper_options.append("rock")
                paper_options.append("rock")
                paper_options.append("paper")
            ran_num = random.randint(0,5)
            computer_input = paper_options[ran_num]
            print("The program picks", computer_input, ".")
            del paper_options[3]
            del paper_options[3]
            del paper_options[3]

        elif user_input == "scissor":
            scissor_options = options
            if len(scissor_options) < 6:
                scissor_options.append("scissor")
                scissor_options.append("paper")
                scissor_options.append("paper")
            ran_num = random.randint(0,5)
            computer_input = scissor_options[ran_num]
            print("The program picks", computer_input, ".")
            del scissor_options[3]
            del scissor_options[3]
            del scissor_options[3]    

        if user_input == "rock" and computer_input == "scissor":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")

        elif user_input == "paper" and computer_input == "rock":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")
        
        elif user_input == "scissor" and computer_input == "paper":
            print("You won", bet, " dollars.")
            user_wins += 1
            money += bet
            print("You have", money, " dollars now.")
        
        elif user_input == computer_input:
            print("Draw!")
            print("You have", money, " dollars now.")
        
        else:
            print("You lost!")
            computer_wins += 1
            money -= bet
            print("You have", money, " dollars now.")

user_win()

owed_money = borrow_money - money
won_money = money - 1000

if borrow_money > 0:
    print("You owe me ", owed_money, " dollars.")
    print("Will you make the payment via kidney?")
else:
    print("You won", won_money, "dollars.")
    print("Your final amount is", money, "dollars")