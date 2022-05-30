import random

lower = int(input("Enter a number for lower limit less than 1000 : "))
upper = int(input("Enter a number for upper limit less than 1000 : "))

for i in range(lower, upper+1):
    if i % 2 == 0:
        print(i)
