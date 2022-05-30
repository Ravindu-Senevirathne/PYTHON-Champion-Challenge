import random

List = []

n = 0
d = 0

for x in range(100):
    List.append(random.randrange(-100, 100))
    
print(List)

if List[n] % 6 == 0:
    d = 5
else:
    d = -1

if d > 0:
    print(List[0], "is divisible by 2 and 3.")
else:
    print(List[0], "is not divisible by 2 and 3.")
