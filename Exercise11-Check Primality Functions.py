num = int(input("Please Enter a number to check if it is Prime:" ))
x = range(2, num+1)
divisors = []
for i in x:
    if num % i == 0:
        if i != num and i != 1:
            divisors.append(i)

if len(divisors) == 0:
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")
