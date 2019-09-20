
import random

a = []
b = []
while len(a) < 10:
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))
print(a)
print(b)
print(set(a) & set(b))
