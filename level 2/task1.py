# task 1

import random

x = random.randint(1,100)
a = None
# print(x)

while x != a:
    try:
        a = a = int(input("enter any number between 1 to 100 : "))
        if a < x:
            print("too low")
        elif a > x:
            print("too high")
        else:
            print("you got it")
    except ValueError:
        print("enter valid number : ")