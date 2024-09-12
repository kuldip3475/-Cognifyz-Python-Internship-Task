# task 2

import random

a1 = int(input("starting number : "))
a2 = int(input("end number : "))

x = random.randint(a1,a2)
a = None
# print(x)

while x != a:
    try:
        a = int(input(f"enter any number between {a1} to {a2} : "))
        if a < x:
            print("too low")
        elif a > x:
            print("too high")
        else:
            print("you got it")
    except ValueError:
        print("enter valid number : ")