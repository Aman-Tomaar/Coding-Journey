# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    num = int(input("Enter a number: "))
    print(1 / num)
except ZeroDivisionError:
    print("Number should be grater then 0")
except ValueError:
    print("Please enter a valid number")
except Exception:
    print("Somthing Went Wrong")
finally:
    print("Finally runs anyway whether there is any exception or not ")
