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
        print "You have 7 energy levels, which is the maximum amount of energy you can have. Everytime you answer a question incorrectly, you'll loose your energy level."
        Playerdecision_2 = raw_input("Do you want to play the game? ")
        return yesno (Playerdecision_2)
    if decision = "yes":
        print "Good Luck!"
    elif decision == "no":
        print "Good Bye."
q1ans = raw_input("QUESTION: What color sweat do hippos have when they are upset? ")
q2ans = raw_input ("QUESTION: Are tomatoes fruits or vegetables? ")
q3ans = raw_input ("QUESTION: What is the fear of fun called? ")
q4ans = raw_input ("QUESTION: Which was the 1st non Test playing country to beat India in an international match?")
q5ans = raw_input ("QUESTION: The nickname of Glenn McGrath is what?" )
q6ans = raw_input ("QUESTION: Nuclear sizes are expressed in what unit name?")
q7ans = raw_input ("QUESTION: Light from the Sun reaches us in how many minutes")
q8ans = raw_input ("QUESTION: A teetotaler is a person that never drinks what?")
q9ans = raw_input ("QUESTION: The lowest natural temperature ever directly recorded at ground level was measured on what Continent?")
q10ans = raw_input ("QUESTION: What was first feature length animated film?")

def challenge():
        if random.random() > 0.5:
            bonus = raw_input ("What’s the name for excessive bodily hair growth in women?")
            return bonus
        
def onequestion(ans):
    if ans == "red":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
        
def twoquestion (q):
    if ans == "vegetables":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def threequestion (q):
    if ans == "Cherophobia":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def fourquestion (q):
    if ans == "sri lanka":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def fivequestion (q):
    if ans == "Penguin":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def sixquestion (q):
    if ans == "Fermi":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def sevenquestion (q):
    if ans == "1":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def eightquestion (q):
    if ans == "alcohol":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def ninequestion (q):
    if ans == "antarctica":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0
def tenquestion (q):
    if ans == "snow white":
        return 1
        print "Correct! You are one step closer to the exit!."
    else:
        print "Wrong!! You have one less energy level "
        return 0


total = treasureboxes(q1ans) + firstquestion() + secondquestion()





    
        


    
    
def main ():
    Playerdecision = raw_input("Do you want to enter to cave? ")
    answer = caveentrance (Playerdecision)
    treasureboxes (answer)
    
    
main()
