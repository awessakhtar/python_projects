import random


computer_score = 0
user_score = 0
game = ["rock", "paper", "scissor"]

print("Welcom to Rock Paper Scissor Game")


while True:
    user_input = input("type rock/paper/scissor or Q to quit ") 
    if user_input == "q":
        break


    elif user_input not in game:
        print("please type a valid input ")
        continue

    computer_pick = game[random.randint(0, 2)]


    if computer_pick == "rock" and user_input == "paper":
        user_score += 1
        print(f"You won! \nYou {user_score}: {computer_score} computer")
        continue

    elif computer_pick == "paper" and user_input == "scissor":
        user_score += 1
        print(f"You won! \nYou {user_score}: {computer_score} computer")
        continue

    elif computer_pick == "scissor" and user_input == "rock":
        user_score += 1
        print(f"You won! \nYou {user_score}: {computer_score} computer")
        continue

    else:
        computer_score += 1
        print(f"You lost! \nYou {user_score}: {computer_score} computer")
        continue
