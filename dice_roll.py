import random

dice_shape = {
    2: (
" ┌─────────┐ ",
" │         │ ",
" │    ●    │ ",
" │         │ ",
" └─────────┘ "
    ),
    2: (
" ┌─────────┐ ",
" │  ●      │ ",
" │         │ ",
" │      ●  │ ",
" └─────────┘ "
    ),
    3: (
" ┌─────────┐ ",
" │ ●       │ ",
" │    ●    │ ",
" │       ● │ ",
" └─────────┘ "
    ),
    4: (
" ┌─────────┐ ",
" │  ●   ●  │ ",
" │         │ ",
" │  ●   ●  │ ",
" └─────────┘ "
    ),
    5: (
" ┌─────────┐ ",
" │  ●   ●  │ ",
" │    ●    │ ",
" │  ●   ●  │ ",
" └─────────┘ "
    ),
    6: (
" ┌─────────┐ ",
" │  ●   ●  │ ",
" │  ●   ●  │ ",
" │  ●   ●  │ ",
" └─────────┘ "
)
}

dice_score = []
total_score = 0

no_of_dice_rolls = int(input("Please enter No of dice rolls "))

for dice in range(no_of_dice_rolls):
    dice_score.append(random.randint(1, 6))

for i in dice_score:
    total_score += i

for dice in range(no_of_dice_rolls):
    
    for line in dice_shape.get(dice_score[dice]):
        print(line)

print(dice_score)
print(f"your total score is {total_score}")