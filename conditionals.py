import random
# You are playing a game called "The Amagi Brilliant Park."
# This game will be played in a cave and you'll have an amount of energy in your body.
# You will be asked if you want to enter the cave or not.
# If you choose to enter the cave, it will ask you which way you would like to go.
# While playing the game,questions will be asked between you and the monsters. 
# If you answer them correctly, you'll be rewarded with weapon to kill the monsters or something that gives you energy.
# If you answer them incorrectly, you'll loose parts of your energy.
# Try to survive!

def caveentrance (decision):
    if decision == "yes":
        print "There are two possible ways you can go after you enter the cave."
        Playerdecision_2 = raw_input("Do you want to enter the left tunnle or the right tunnle?")
        leftorright (Playerdecision_2)
    elif decision == "no":
        print "Good Bye."
   
def leftorright (decision_2):
    if decision_2 == "left":
        print "The monster is waiting for you inside the cave. You have no weapons and you cannot choose to quit. This means that you'll loose parts of their energy!"
    elif decision_2 == "right":
        print "You are lucky! No monsters!"
    
    
    

        

def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    caveentrance (Playerdecision)
    Seconddecision = raw_input ("There are two tresure boxes placed infront of you, would you like to open the left one or the right one?")
    
    
    


    

    
main()
