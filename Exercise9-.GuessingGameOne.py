import random
number = random.randint(1, 10)
user = input("Please guess a number between 1 to 9: ")


def takeinput(user):
    if user == "exit":
        print("Thanks For playing the game")
        exit()
    else:
        game(number, int(user))


def game(num, numuser):
    if num == numuser:
        print("Exactly Right " + str(num) + " was system's number")
    elif num > numuser:
        if num-numuser > 3:
            print("guess is too low... " + str(num) + " was system's number")
        else:
            print("slightly low..." + str(num) + " was system's number")
    else:
        if numuser-num > 3:
            print("guess is too high... " + str(num) + " was system's number")
        else:
            print("slightly high..." + str(num) + " was system's number")

takeinput(user)