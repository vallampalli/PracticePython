num = int(input("Please enter a num: "))
x = range(1, num+1)
divisors = []
for i in x:
    if num % i == 0:
        divisors.append(i)
print("The divisors the " + str(num) + " is " + str(divisors))