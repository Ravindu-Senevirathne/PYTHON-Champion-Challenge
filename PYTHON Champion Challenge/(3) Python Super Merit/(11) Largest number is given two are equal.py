X = int(input("Enter a number for X : "))
Y = int(input("Enter a number for Y : "))
Z = int(input("Enter a number for Z : "))

if X == Y:
    if X > Y and X > Y:
        print("X is the largest.")
    elif Y > X and Y > Z:
        print("Y is the largest.")
    elif Z > X and Z > Y:
        print("Z is the largest.")

if X == Z:
    if X > Y and X > Y:
        print("X is the largest.")
    elif Y > X and Y > Z:
        print("Y is the largest.")
    elif Z > X and Z > Y:
        print("Z is the largest.")

if Z == Y:
    if X > Y and X > Y:
        print("X is the largest.")
    elif Y > X and Y > Z:
        print("Y is the largest.")
    elif Z > X and Z > Y:
        print("Z is the largest.")

if X != Y and X != Z and Y != Z:
    print("Two numbers should be equal.")
