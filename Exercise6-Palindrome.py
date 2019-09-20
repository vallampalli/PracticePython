input_string = input("Please enter a string to check if it is palindrome: ")
word = []
reverse = []
for i in input_string:
    if input_string.isalpha():
        word.append(i)
for i in word[::-1]:
    reverse.append(i)

if word == reverse:
    print(input_string + " is a Palindrome")
else:
    print(input_string + " is Not a Palindrome")
