X = int(input("Enter a value for the length of the rectangle : "))
Y = int(input("Enter a value for the breadth of the rectangle : "))

if X == Y:
    print("Length and the breadth are not equal in a rectangle")
else:
    Area = X * Y
    Perimeter = X + X + Y + Y

    print("Area is : ", Area, "cm")
    print("Perimeter is : ", Perimeter, "cm")
