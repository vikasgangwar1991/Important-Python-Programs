#Guess a number
n=18
no_of_guesses=5
while no_of_guesses>=1:
    num=int(input("Guess a number:"))
    if num>18:
        print("You are far from number")
    elif num<18:
        print("you are near to number")
    else:
        print("yes,you are right")
        print("congrats..you won")
        print("you used no.of guessses", (5-no_of_guesses)+1)
        break

    no_of_guesses-=1
    print("No. of guesses left", no_of_guesses)
    if no_of_guesses==0:
        print("game over")
        print("you lost the game")
