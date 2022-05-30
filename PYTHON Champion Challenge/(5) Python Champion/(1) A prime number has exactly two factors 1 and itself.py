number = int(input("Enter a number :"))
factors = 0  
for divisible_number in range(number):
    divisible_number += 1  

    remainder = number % divisible_number
    if remainder == 0:
        factors += 1  
if factors <= 2:  
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
