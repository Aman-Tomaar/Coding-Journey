import random

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
}

dice = []
total = 0

no_dice = int(input("Enter the number of dice you wanna roll: "))

for i in range(no_dice):
    x = random.randint(1, 6)
    for j in dice_art.get(x):
        # or we can use this if you dont wanna make a loop => print(*dice_art.get(x), sep="\n")
        print(j)
    total += x
print(f"TOTAL = {total}")
