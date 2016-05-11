import random
import time
# You are playing a game called "The Amagi Brilliant Park."
# This game will be played in a cave and you'll have an amount of energy in your body.
# If you choose to enter the cave, it will ask you which way you would like to go.
# While playing the game,questions will be asked and you'll have an amount of time to answer the question. (you can search in the internet.)
# If you answer them correctly, you are one step closer to the exit.
# If you answer them incorrectly, you will lose one energy level.
# you can gain more energy from the trasure boxes.
# The goal is to survive through this cave without before running out of energy! (All of them are one word answer.)

def caveentrance (decision):
    if decision == "yes":
        print "You have 7 energy levels, which is the maximum amount of energy you can have. Everytime you answer a question incorrectly, you'll loose your energy level. There are two possible ways you can go after you enter the cave."
        Playerdecision_2 = raw_input("Do you want to enter the left tunnle or the right tunnle?")
        return leftorright (Playerdecision_2)
    elif decision == "no":
        print "Good Bye."
q1ans = ans = raw_input("QUESTION: What color sweat do hippos have when they are upset? ")
   
def leftorright (decision_2):
    if decision_2 == "left":
        
        return ans
    elif decision_2 == "right":
        ans = raw_input ( "QUESTION: Are tomatoes fruits or vegetables? ")
        return ans
def treasureboxes (Seconddecision):
    if Seconddecision == "red":
        print "Correct! You are one step closer to the exit!."
        return 1
    elif Seconddecision == "vegetables":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def firstquestion():
    if firstdecision == "red":
        return 1
    else:
        return 0
def secondquestion ():
    if seconddecision == "vegetables"
        return 1
    else:
        return 0


total = treasureboxes(q1ans) + firstquestion() + secondquestion()





    
        


    
    
def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    answer = caveentrance (Playerdecision)
    treasureboxes (answer)
    
    
main()
