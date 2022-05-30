import random

A = int(input("Gues the number from 1 - 100 : "))
Z = random.randrange(1, 100)

def checking():
    if A > Z:
        print("High")
    elif A < Z:
        print("Low")
    elif A == Z:
        print("You are correct.")

checking()
