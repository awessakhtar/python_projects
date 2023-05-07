import random


print("Welcom to Number Guessing Game")
anwser = input("do you want to play (yes/no)? ")

if anwser != "yes":
    quit()
else:
    user_range = input("enter a range to guess from   ")

    if user_range.isdigit():
        user_range = int(user_range)
        if user_range <= 0:
            print("please provide a valid number next time")
            quit()

 

guess_number = random.randint(0, user_range)
no_of_guess = 0

while True:
    no_of_guess += 1
    user_guess = input("please input your guess number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess <= 0:
        print("please input postive number next time")
        quit()
        
    if user_guess == guess_number:
        print("you got it correct, Congradulations!")
        break
    else:
        print("wrong answer")
        continue
print("you got it in", no_of_guess, "guesses")