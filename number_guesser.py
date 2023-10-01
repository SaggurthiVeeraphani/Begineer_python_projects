import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("Please type number larger than 0 next time.")
        quit()
else:
    print("Please type the number next time.")
    quit()

random_number = random.randint(0,top_of_range)
guess_count = 0

while True:
    guess_count += 1
    guess_number = input("Please guess the number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("please guess the number again")
        continue

    if guess_number == random_number:
        print("you guessed the correct number!")
        break
    elif guess_number < random_number:
        print("you are below the number")
    else:
        print("you are above the number")

print("you got it in", guess_count,"guesses")  
