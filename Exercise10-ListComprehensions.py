import random
x = random.sample(range(100), 25)
y = random.sample(range(100), 40)
x.append(25)
x.append(25)
y.append(25)

result_with_possible_duplicates = [a for a in x if a in y]

result_no_duplicates_using_for_loop = []

result_no_duplicates_set = [a for a in set(x) if a in y]

for i in result_with_possible_duplicates:
    if i not in result_no_duplicates_using_for_loop:
        result_no_duplicates_using_for_loop.append(i)

print(x)
print(y)
print(sorted(result_with_possible_duplicates))

print(sorted(result_no_duplicates_using_for_loop))
print(result_no_duplicates_set)
