#  variable scope = where the variable is visible & accessible
# scope resolution = (LEGB rule) Local, Enclosing, Global, Built-in

print("1. Local scope")


def func1():
    x = 10  # local variable
    print(x)  # accessible here


def func2():
    x = 20  # local variable
    print(x)  # accessible here


func1()
func2()

print("\n2. Enclosed scope")


def func3():
    x = 30  # local variable

    def func4():
        print(x)  # accessible here (enclosed scope)

    func4()


func3()

print("\n3. Global scope")

x = 40  # global variable


def func5():
    print(x)  # accessible here (global scope)


func5()

print("\n4. Built-in scope")
from math import e


def func6():
    print(e)  # accessible here (built-in scope)


e = 5  ## local variable (overrides built-in variable) if e wasn't defined as local variable then it will print built-in variable value i.e 2.718281828459045
func6()

from math import pi


def func7():
    print(pi)  # accessible here (built-in scope)


func7()
