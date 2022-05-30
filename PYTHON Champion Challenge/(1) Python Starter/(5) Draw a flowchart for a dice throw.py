import random

running = True
while running:
    picking = random.randrange(1, 6)
    if picking == 1:
        print("Rolled number is 1")
        running = False
    elif picking == 2:
        print("Rolled number is 2")
        running = False
    elif picking == 3:
        print("Rolled number is 3")
        running = False
    elif picking == 4:
        print("Rolled number is 4")
        running = False
    elif picking == 5:
        print("Rolled number is 5")
        running = False
    else:
        print("Rolled number is 6")
        running = False
