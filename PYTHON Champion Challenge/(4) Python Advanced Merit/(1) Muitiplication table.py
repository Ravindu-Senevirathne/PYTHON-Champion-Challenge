a = int(input("Enter a number : "))
n = 0

while True:
    print(a, "*", n+1, "=", a*(n+1))
    n += 1

    if n == 10:
        break
