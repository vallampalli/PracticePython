a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
new = []
for i in a:
    if i < 5:
        new.append(i)
print(new)"""
new = [i for i in a if i < 10]
print(new)

print([i for i in a if i < 10])
