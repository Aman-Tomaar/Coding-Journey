import random

rnum = random.randint(1, 100)
score = 10
print(
    "RULES :"
    "\n1. You need to guess a number Between 1-100"
    "\n2. You got 10 trys if you cant find it in 10 trys you losse "
)

while score > 0:
    guess = int(input("Enter a Number between 1-100: "))
    if guess == rnum:
        print(
            "------------------------\n"
            "YOU WON!!!\n"
            "You guessd the number !!!\n"
            f"Your score is {score}\n"
            "------------------------\n"
        )
        if score == 10:
            print(
                "WHAT WHAT!!!!!\n"
                "*********************************************************************************\n"
                "YOU GOT A PERFECT SCORE THIS HASN'T HAPPENED IN A MILLION YEARS!!!\nYOU ARE A GOD!!!!\n"
                "*********************************************************************************"
            )
        break
    elif guess < rnum and guess >= 0:
        print(f"The number is grater than {guess}")
        score -= 1
    elif guess > rnum and guess <= 101:
        print(f"The number is less than {guess}")
        score -= 1
    else:
        print(
            "Are you DUMB ? Number is b/w 1-100. It can't be less than 1 or grater than 100.\n"
            "You are panalized you score is dedcuted by 2"
        )
        score -= 2
if score < 1:
    print(
        f"\n\nYOU LOOSE!!!\nYour score got less than 1 and you are definately DUMB !!!\nThe Number was {rnum}!!!"
    )
