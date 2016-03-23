import random
# You are playing a game called "The Amagi Brilliant Park."
# This game will be played in a cave.
# You will be asked if you want to enter the cave or not.
# If you choose to enter the cave, it will print the instructions of this game.
# If you can find the exit of this game, you'll be rewarded.

def caveentrance (decision):
    if decision == "yes":
        print Playerdecision_2
    elif decision == "no":
        print "Good bye"


def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    print "There are two possible ways you can go after you enter the cave."
    Playerdecision_2 = raw_input("Do you want to enter the left tunnle or the right tunnle?")
    
    
main()
