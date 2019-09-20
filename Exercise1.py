from datetime import datetime
name = input("Please Enter Your Name: ")
age = int(input("Please enter your age: "))
year = datetime.now()
current_year = year.year
years_to_hundred = 100 - age
turn_hundred = current_year + years_to_hundred
message = "Hello " + name + ", you will turn Hundred at year " + str(turn_hundred) + "\n"
print(4*message)
