a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
input = int(input("Please Enter a Number: "))
LowerThanUserEnteredNum = []
for i in a:
    if i < input:
        LowerThanUserEnteredNum.append(i)
print(LowerThanUserEnteredNum)


