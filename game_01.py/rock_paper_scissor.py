# Rock paper scissor
# rock beats scissor , scissor beats paper and paper beats rock

import random
import sys

def menu():
    print("="*50)
    print("\tLets start the game")
    print("="*50)
    print("\tchoose 1 to 3 for :")
    print("\t1 for Rock")
    print("\t2 for Paper")
    print("\t3 for Scissor")
    print("\t4 for Exit the game....")
    print("="*50)

# main program
while(True):
    menu()
    user =  int(input("choose the 1 to 3 numbers : "))
    match(user):
        case 1:
            print("User = 1")
            computer=(random.randint(1,3))
            print("computer = {}".format(computer))
            if(computer==1):
                print("Draw")
            elif(computer==2):
                print("Computer win and u lose")
            else:
                print("You win")
        case 2:
            print("User = 2")
            computer=(random.randint(1,3))
            print("computer = {}".format(computer))
            if(computer==1):
                print("You win")
            elif(computer==2):
                print("Draw")
            else:
                print("Computer win and You lose")
        case 3:
            print("User = 3")
            computer=(random.randint(1,3))
            print("computer = {}".format(computer))
            if(computer==1):
                print("Computer win and u lose")
            elif(computer==2):
                print("You win")
            else:
                print("Draw")
        case 4:
            print("You are going to out of game")
            sys.exit()
        case _:
            print("Ur Input is wrong----try again")