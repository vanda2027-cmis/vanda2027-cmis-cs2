import random
import time
# You are playing a game called "The Amagi Brilliant Park."
# This game will be played in a cave and you'll have an amount of energy in your body.
# If you choose to enter the cave, it will ask you which way you would like to go.
# While playing the game,questions will be asked between you and the monsters. 
# If you answer them correctly, you'll be rewarded with weapons to kill the monsters or food that gives you energy.
# If you answer them incorrectly, the monsters will hurt you and you'll loose parts of energy. If you loose all of your energy, you are dead.
# The goal is to survive through this cave without getting killed.

def caveentrance (decision):
    if decision == "yes":
        print "You have 20 energy levels, which is the maximum amount of energy you can have. Everytime you answer a question incorrectly, you'll loose your energy level. There are two possible ways you can go after you enter the cave."
        Playerdecision_2 = raw_input("Do you want to enter the left tunnle or the right tunnle?")
        leftorright (Playerdecision_2)
    elif decision == "no":
        print "Good Bye."
        
   
def leftorright (decision_2):
    if decision_2 == "left":
        print "The monster is waiting for you inside the cave. You have no weapons and you cannot choose to quit! ENERGY LEVEL: 19"
    elif decision_2 == "right":
        print "You are lucky! No monsters! ENERGY LEVEL: 20"
def treasureboxes (Seconddecision):
    if Seconddecision == "1":
        print "You are rewarded with food that gives you 1 energy level."
    elif Seconddecision == "2":
        print "You got a free pass! This means that you can choose to not answer 1 question."
    else:
        print "Too bad! Nothing in the box!"
    
start = time.time(30)
    print("You have 30 seconds!!")
end = time.time(30)


    
    
    

        

def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    caveentrance (Playerdecision)
    Seconddecision = raw_input ("There are 5 tresure boxes placed infront of you, which one would you like to open 1, 2, 3 ,4 ,or 5")
    treasureboxes (Seconddecision)
    Question1 = raw_input ("
    
    
    


    

    
main()
