bal = 0


def balance(bal):
    print(f"Checking Balance......\n₹{bal}\n********************")
    return bal


def deposit(bal):
    d_money = int(input("Enter the amount you want to deposit: ₹"))
    if d_money <= 0:
        print(
            "!!! Invalid amount. Must be greater than zero. !!!\n********************"
        )
        return bal

    bal += d_money
    print(
        f"Depositing amount ₹{d_money} in your account.......\n!!! ₹{d_money} SUCCESSFULLY DEPOSITED !!!\n********************"
    )
    return bal


def withdraw(bal):
    w_money = int(input("Enter the amount you want to withdraw: ₹"))
    if w_money <= 0:
        print(
            "!!! Invalid amount. Must be greater than zero. !!!\n********************"
        )
        return bal

    if w_money > bal:
        print("!!! INSUFFICIENT BALANCE !!!\n********************")
        return bal

    bal -= w_money
    print(
        f"Withdrawing amount ₹{w_money} from your account.......\n!!! ₹{w_money} SUCCESSFULLY WITHDRAWN !!!\n********************"
    )
    return bal


print(f"********************\n{"BANKING PROGRAM":^20}\n********************")
while True:
    try:
        u_choice = int(
            input(
                "1. Check Balance\n2. Deposit\n3. Withdraw\n4. EXIT THE BANK\nYour Choice: "
            )
        )
    except ValueError:
        print("\nInvalid input! Please enter a number from 1 to 4.\n")
        continue

    print()
    if u_choice == 1:
        balance(bal)
    elif u_choice == 2:
        bal = deposit(bal)
    elif u_choice == 3:
        bal = withdraw(bal)
    elif u_choice == 4:
        print("!! EXITING THE BANK. THANK YOU! !Z")
        break
    else:
        print("INVALID INPUT TRY AGAIN......\n")
