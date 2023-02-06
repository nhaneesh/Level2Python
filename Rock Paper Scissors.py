#import random
from random import *
#from random import randint
import time
t = ["rock","paper","scissor"]
#computer = random.choice(t)
#computer = (t[randint(0,2)])
#print(computer)
player = False
while player == False :
    computer = (t[randint(0,2)])
    player = input("Please choose one from Rock,Paper,Scissor?").lower()
    #player = player.lower()
    #print(player)
    if player == computer:
        time.sleep(2)
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
            time.sleep(2)
            print("Computer chooses ",computer)
            
            print("You lose , ",computer," covers ",player)
        else :
            time.sleep(2)
            print("Computer chooses ",computer)
            print("You win , ",player," smashes ",computer)
    elif player == "paper":
        if computer == "scissor":
            time.sleep(2)
            print("Computer chooses ",computer)
            print("You lose , ",computer," cuts ",player)
        else :
            time.sleep(2)
            print("Computer chooses ",computer)
            print("You win , ",player," covers ",computer)
    elif player == "scissor" :
        if computer == "rock":
            time.sleep(2)
            print("Computer chooses ",computer)
            print("You lose , ",computer," smashes ",player)
        else :
            time.sleep(2)
            print("Computer chooses ",computer)
            print("You win , ",player," cuts ",computer)
    else :
        print("Invalid response")
    player = False
    print(computer)
