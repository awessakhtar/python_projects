user_name = input("type your name ")
print("welcom", user_name)

answer = input("you are on glass square turn left/right to discover :").lower()
if answer not in ["left", "right"]:
    print("game over!")
    quit()
elif answer == "left":
    print("Game lost!,  be aware of the traffic")
else:
    answer = input("There is a bridge up front do want to go by bridge or swim ").lower()
    if answer == "swim":
        print("Game over, beaware of crocodiles")
        quit()
    else:
        print("you win")
        quit()