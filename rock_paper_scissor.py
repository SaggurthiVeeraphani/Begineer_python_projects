import random

user_wins = 0
computer_wins = 0

options = ["rock","scissors","paper"]

while True:
    user_input = input("Type Rock/Paper/scissors or q to quit(): ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_input = options[random_number]
    print("computer picked",computer_input,".")

    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won",user_wins,"times.")
print("The Computer won",computer_wins,"times.")
print("Goodbye!")
    


    


