print("1. Celsius")
print("2. Fahrenheit")
i = input("Which item, you want to convert into the other : ")

if i == '1':
    C = input("Enter the temperature in Celsius : ")
    C = float(C)

    F = (9.0/5.0 * C) + 32
    print("Temperature in Fahrenheit : ", F)


elif i == '2':
    X = input("Enter the temperature in Fahrenheit : ")
    X = float(X)

    Y = 5.0/9.0 * (X - 32)
    print("Temperature in Celsius : ", Y)
else:
    print("Entered number is invalid.")
