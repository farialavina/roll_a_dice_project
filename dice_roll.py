import random

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
1: ("┌───────┐",
    "│       │",
    "│   ●   │",
    "│       │",
    "└───────┘" ),
2 :("┌───────┐",
    "│ ●     │",
    "│       │",
    "│     ● │",
    "└───────┘" ), 
3 :("┌───────┐",
    "│ ●     │",
    "│   ●   │",
    "│     ● │",
    "└───────┘" ),
4 :("┌───────┐",
    "│ ●   ● │",
    "│       │",
    "│ ●   ● │",
    "└───────┘" ),
5 :("┌───────┐",
    "│ ●   ● │",
    "│   ●   │",
    "│ ●   ● │",
    "└───────┘" ),
6 :("┌───────┐",
    "│ ●   ● │",
    "│ ●   ● │",
    "│ ●   ● │",
    "└───────┘" )

}

dice = []
total = 0

rolls = int(input("How many times roll a dice?  "))

random.randint(1, 6)
for roll in range(rolls):
    dice.append(random.randint(1, 6))

# for roll in range(rolls):
#     for line in dice_art.get(dice[roll]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = '')
    print()        

for die in dice:
    total+= die
print(f"The total is {total}")       

    
