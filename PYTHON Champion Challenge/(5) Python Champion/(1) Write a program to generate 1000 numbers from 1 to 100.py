import random
g = []

for ge in range(1000):
    #101 for 100
    
    g.append(random.randrange(1,101))

print("Generated 1000 numbers :")
print()
print(g)

print("\nSimilar numbers :")
print()
counts = [[print(item,"has",g.count(item),"numbers")] for item in set(g)]
