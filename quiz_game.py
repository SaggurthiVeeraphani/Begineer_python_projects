print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != 'yes':
    quit()

print("Okay! let's play :-) ")
score = 0

answer = input("1.what is the national animal of India? ").lower()
if answer == "tiger":
    score += 1
    print("correct!")
else:
    print("Wrong")

answer = input("2.what is the national sport of India? ").lower()
if answer == "hockey":
    score += 1
    print("correct!")
else:
    print("Wrong")

answer = input("3.who is the captain of Indian cricket team? ").lower()
if answer == "rohit sharma":
    score += 1
    print("correct!")
else:
    print("Wrong")

answer = input("4.who designed the national flag of india? ").lower()
if answer == "pingali venkayya":
    score += 1
    print("correct!")
else:
    print("Wrong")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
   