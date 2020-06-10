import random

P1 = input("Let's play Rock/Paper/Scissors! What's your name? > ")
def game_count():

    while True:
        play_count =input("How many games would you like to play? > " )
        try :
            play_count =int(play_count)
            if play_count >= 1:
                return play_count
            else:
                print("Input has to be bigger than 1. ")

        except ValueError:
            print("{} is not a number.".format(play_count))

def play_again():

    print("Would you like to play again?")
    while True :
        again = input("Type Y for Yes,N for No > ")
        if again == "Y":
            RPS()

        elif again == "N":
            print("See you again!")
            quit()

        else:
            print("Invalid input ")

def RPS():
    game = game_count()
    win_count = 0

    i = 0
    while i < game:
        RPS = ["Rock","Paper","Scissors","Paper","Rock","Scissors"]
        CP = RPS[random.randint(0,5)]
        player = input("<{0}>  {1} ,Rock/Paper/Scissors? ".format((i+1),P1))

        if player == CP:
            print("Computer picks {}".format(CP))
            print("It's a tie !")
            i += 1
        elif player == "Rock":
            if CP == "Paper":
                print("Computer picks {}".format(CP))
                print("You lose! ")
                i += 1
            else :
                print("Computer picks {}".format(CP))
                print("You win! ")
                i += 1
                win_count += 1

        elif player == "Paper":
            if CP == "Scissors":
                print("Computer picks {}".format(CP))
                print("You lose! ")
                i += 1
            else :
                print("Computer picks {}".format(CP))
                print("You win! ")
                i += 1
                win_count += 1

        elif player == "Scissors":
            if CP == "Rock":
                print("Computer picks {}".format(CP))
                print("You lose! ")
                i += 1
            else :
                print("Computer picks {}".format(CP))
                print("You win! ")
                i += 1
                win_count+= 1

        else:
            print("Invalid input.Check your spelling ! ")

    print("You win {} out of {} games! \n".format(win_count,game))

    play_again()

RPS()

