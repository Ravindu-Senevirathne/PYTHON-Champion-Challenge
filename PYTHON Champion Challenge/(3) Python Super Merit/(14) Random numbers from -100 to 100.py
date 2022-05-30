import random

list1 = []

for x in range(100):
    list1.append(random.randrange(-100, 100))
    
print(list1)

Maximum = max(list1)
Minimum = min(list1)

print("Largest number : ", Maximum)
print("Smallest number : ", Minimum)

Difference = Maximum - Minimum

print("Difference is : ", Difference)
