import random

score = 0
# ROCK 1
# PAPER 2
# SCISSORS 3
while True:
    ans = random.choice([1, 2, 3])
    user = int(input("Enter your choice [1: Rock, 2: Paper, 3:Scissors] (0 to quit):"))

    if user == 0:
        break
    elif user == 1:
        print("You Choose : ROCK")
        if ans == 1:
            print("Computer Choose ROCK\nTIE!")
        elif ans == 2:
            print("Computer Choose PAPER\nYou LOOSE")
            score -= 1
        elif ans == 3:
            print("Computer Choose SCISSORS\nYou WON")
            score += 1
    elif user == 2:
        print("You Choose : PAPER")
        if ans == 1:
            print("Computer Choose ROCK\nYou WON")
            score += 1
        elif ans == 2:
            print("Computer Choose PAPER\nTIE!")
        elif ans == 3:
            print("Computer Choose Scissors\nYou LOOSE")
            score -= 1
    elif user == 3:
        print("You Choose : SCISSORS")
        if ans == 1:
            print("Computer Choose ROCK\nYou LOOSE")
            score -= 1
        elif ans == 2:
            print("Computer Choose PAPER\nYou WON")
            score += 1
        elif ans == 3:
            print("Computer Choose SCISSORS\nTIE!")
    print()
print("\n********************************")
if score == 0:
    print(f"You TIED! Your score is {score}")
elif score > 0:
    print(f"Your WON! Your score is {score} ^-^")
elif score < 0:
    print(f"Your LOOSE! Your score is {score} :[")
print("********************************")
