import time

answer = input("Do you want to play Hangman Game? y/n ").lower()

if answer == 'n':
    exit()


name = input("Please Enter your name: ")
print(f"Welcome, {name} to Hangman Game")

word = 'python'

# wait for 1 second
time.sleep(1)

print("start guessing now ... ")
time.sleep(0.5)

guesses = []
turns = 10
while True:
    while turns > 0:
        failed = 0

        # check from the word by characters
        for c in word:
            # check if the same character entered by the user
            if c in guesses:
                # print if character matches with user
                print(c, end='')

            else:
                #when character not found
                print("_", end="")
                failed += 1
        # now the user have entered all the characters and time to put out the results
        if failed == 0:
            print("\nYOU WON, WELDONE")
            break

        # now take input from user to guess a charachter
        guess = input(" Guess a charcter : ")
        guesses += guess

        # when the guess is wrong
        if guess not in word:
            print("Wrong Guess ")
            turns -= 1
    
    if turns == 0:
        print ("\nYou Lost, Better Luck next time")
    print(f"\n your Scroe is {turns +5} out of 10")
    again = input("\n Do you want to play agai? y/n ").lower()

    if again == "y":
        continue
    else:
        break

