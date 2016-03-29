import random
# You are playing a game called "The Amagi Brilliant Park."
# This game will be played in a cave.
# You will be asked if you want to enter the cave or not.
# If you choose to enter the cave, it will ask you which way you would like to go.
# While playing the game,questions will be asked and you have to answer them correctly.
# If you answer them correctly, you'll be rewarded with weapon and try to exit the cave.-

def caveentrance (decision):
    if decision == "yes":
        print "There are two possible ways you can go after you enter the cave."
        Playerdecision_2 = raw_input("Do you want to enter the left tunnle or the right tunnle?")
        leftorright (Playerdecision_2)
    elif decision == "no":
        print "Good Bye."
   
def leftorright (decision_2):
    if decision_2 == "left":
        print "The weapon given to you is a sword. Use them to fight with the monster that's going to appear in this pathway!"
    elif decision_2 == "right":
        print "You are lucky! No monsters!"
    
    
    

        

def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    caveentrance (Playerdecision)
    
    
    
    


    

    
main()
