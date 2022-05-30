X = int(input("Enter a number for X : "))
Y = int(input("Enter a number for Y : "))
Z = int(input("Enter a number for Z : "))

if X < Y and X < Z:
    print("X is the smallest.")
elif Y < X and Y < Z:
    print("Y is the smallest.")
elif Z < X and Z < Y:
    print("Z is the smallest.")
