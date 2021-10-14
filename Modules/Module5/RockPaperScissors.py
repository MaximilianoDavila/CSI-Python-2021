import random
def main ():
    print ("Welcome to Rock, Paper, Scissors Game. You will lose anyway im a computer afterall.")
    RPS = ["rock" , "paper" , "scissors"]
    Play_again = "y"

    while Play_again == "y":
        Playerchoice = input("now lets get with the game so, choice one: rock, paper, scissors. \n")
        Computerchoice = random.choice(RPS)

        print (f"Computer selected:{Computerchoice}")
        print(f"Player selected: {Playerchoice}")

        if(Playerchoice == Computerchoice):
            print("Wow we tied, now i feel stupid for saying that :/")
        elif(Playerchoice == "rock" and Computerchoice == "paper"):
            print("Paper covers rock, I knew you lost. I am a computer after all :|")
        elif(Playerchoice == "scissors" and Computerchoice == "paper"):
            print("Scissors beats paper, wow i lost now i feel stupid :/")
        elif(Playerchoice == "rock" and Computerchoice == "scissors"):
            print("rock beats scissors, no way how did I lose maaan :[")
        elif(Playerchoice == "paper" and Computerchoice == "scissors"):
            print("Yes I won! scissor beats paper! I mean what did you expect huh, I am a computer after all")
        elif(Playerchoice == "paper" and Computerchoice == "rock"):
            print("paper beats rock. No way! how am I losing!")
        elif(Playerchoice == "scissors" and Computerchoice == "rock"):
            print("Rock beats paper, Yes I won!")
        else:
            print("Something isn,t right. Maybe try again")
        Play_again = input('play again? Enter "y" for yes or "n" for no')
    print("Game comcluded.")
main()
