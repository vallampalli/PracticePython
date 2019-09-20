
def rps():
    menu = input("Press 'Y' to play again!")

    if menu == "Y":
        playerOne = input("Please Says Rock, Paper Or Scissors")
        playerTwo = input("Please Says Rock, Paper Or Scissors")
        while playerOne != playerTwo:
            if playerOne == "scissors" and playerTwo == "rock":
                print("Player 2 Wins: Rock Beats Scissors")
                rps()
            elif playerOne == "rock" and playerTwo == "scissors":
                print("Player 1 Wins: Rock Beats Scissors")
                rps()
            elif playerOne == "paper" and playerTwo == "scissors":
                print("Player 2 Wins: Scissors beats Paper")
                rps()
            elif playerOne == "scissors" and playerTwo == "paper":
                print("Player 1 Wins: Scissors beats Paper")
                rps()
            elif playerOne == "rock" and playerTwo == "paper":
                print("Player 2 Wins: Paper Beats Rock")
                rps()
            elif playerOne == "paper" and playerTwo == "rock":
                print("Player 1 Wins: Paper Beats Rock")
                rps()
        print("Both Players Entered Same Thing! So Try Again")
        rps()
    else:
        print("Thanks For Playing Rock, Paper and Scissors!!!")


rps()