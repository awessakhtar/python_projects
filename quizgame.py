print("Welcome to quiz game")

playing = input("Do you want to play? (yes/ no)  ")
if playing != "yes":
    quit()

print("Ok lets Play")
score = 0
answer = input("input short form of Central Processing Unit ? ")
if answer.lower() == "cpu":
    score += 1
    print(f"Correct Answer you got {score} Correct")
    
else:
    print("incrorect")
answer = input("input short form of Graphic Processing Unit ? ")
if answer.lower() == "gpu":
    score += 1
    print(f"Correct Answer you got {score} Correct")
else:
    print("incrorect")

answer = input("input short form of Random Acess Memory? ")
if answer.lower() == "ram":
    score += 1
    print(f"Correct Answer you got {score} Correct")
else:
    print("incrorect")


print(f"You got {score} Correct")

print(f"You got {(score/3)*100.00} Correct")