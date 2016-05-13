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

def caveentrance ():
    decision = raw_input("Do you want to enter the cave?")
    if decision == "yes":
        print "You have 5 energy levels, which is the maximum amount of energy you can have. Everytime you answer a question incorrectly, you'll lose your energy level."
        print "Good Luck!"
    elif decision == "no":
        print "Good Bye."
        quit()
want = raw_input ("Do you really want to play this game?")
def doyoureally(want):
    if want == "yes":
        print "LOL OK"

doyoureally(want)
reallywant = raw_input ("Are you sure ?")

def reallyreally(reallywant):
      if reallywant == "yes":
        print "OKAY! :D"
reallyreally(reallywant)
            

def challenge():
        if randomdecider():
            bonus = raw_input("CHALLENGE: What's the name for excessive bodily hair growth in women?")
            return bonus
        else:
            return None
def challengeresult(challenge):
    if challenge == None:
        return 0
    elif challenge == "Hirsutism":
        return 1
    else:
        return 0
        
def onequestion(ans):
    if ans == "red":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
        
def twoquestion (ans):
    if ans == "vegetables":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def threequestion (ans):
    if ans == "cherophobia":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def fourquestion (ans):
    if ans == "sri lanka":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def fivequestion (ans):
    if ans == "penguin":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def sixquestion (ans):
    if ans == "fermi":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def sevenquestion (ans):
    if ans == "1":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def eightquestion (ans):
    if ans == "alcohol":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def ninequestion (ans):
    if ans == "antarctica":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
def tenquestion (ans):
    if ans == "snow white":
        print "Correct! You are one step closer to the exit!."
        return 1
    else:
        print "Wrong!! You have one less energy level "
        return 0
    
def q1 (ans):
    if ans == "legit goal":
        print "Correct!!!!! :'D"
    else:
        print "Wrong!!!!! :'("
def q2 (ans):
    if ans == "london":
        print "Correct!!!!! :'D"
    else:
        print "Wrong!!!!! :'("
def q3 (ans):
    if ans == "the horror":
        print "Correct!!!!! :'D"
    else:
        print "Wrong!!!!! :'("
def randomq (randomnum):
    if randomnum == 1:
        q1 (raw_input("FINAL: IF YOU GET THIS QUESTION WRONG YOU LOSE: In the 2011/2012 Official Rules of the NBA you will learn the definition of what term on page 21? "))
    elif randomnum == 2:
        q2 (raw_input("FINAL: IF YOU GET THIS QUESTION WRONG YOU LOSE: Early in Conrad's 1903 novella, Marlow makes a comment one of the dark places on earth. About what place does he say this? "))
    elif randomnum == 3:
        q3 (raw_input("FINAL: IF YOU GET THIS QUESTION WRONG YOU LOSE: As Marlow approaches, what are Kurtz's final words? "))

def randomdecider():
    if random.random() > 0.5:
        return True
    else:
        return False
    

def main ():
    caveentrance()
    q1ans = raw_input("QUESTION: What color sweat do hippos have when they are upset? ")
    q1result = onequestion(q1ans)
    q2ans = raw_input ("QUESTION: Are tomatoes fruits or vegetables? ")
    q2result = twoquestion(q2ans)
    q3ans = raw_input ("QUESTION: What is the fear of fun called? ")
    q3result = threequestion(q3ans)
    q4ans = raw_input ("QUESTION: Which was the 1st non Test playing country to beat India in an international match? ")
    q4result = fourquestion(q4ans)
    q5ans = raw_input ("QUESTION: The nickname of Glenn McGrath is what? " )
    q5result = fivequestion(q5ans)
    q6ans = raw_input ("QUESTION: Nuclear sizes are expressed in what unit name? ")
    q6result = sixquestion(q6ans)
    q7ans = raw_input ("QUESTION: Light from the Sun reaches us in how many minutes")
    q7result = sevenquestion(q7ans)
    q8ans = raw_input ("QUESTION: A teetotaler is a person that never drinks what? ")
    q8result = eightquestion(q8ans)
    q9ans = raw_input ("QUESTION: The lowest natural temperature ever directly recorded at ground level was measured on what Continent? ")
    q9result = ninequestion(q9ans)
    q10ans = raw_input ("QUESTION: What was first feature length animated film? ")
    q10result = tenquestion(q10ans)
    total = q1result + q2result + q3result + q4result + q5result + q6result + q7result + q8result + q9result +q10result 
    bonusans = challengeresult(challenge())
    if total + bonusans <= 5:
        out = """You got only {} questions correct!""".format(total)
        print out
    elif total + bonusans >= 6:
        out = """You got {} questions correct!""".format(total)
    randomq(random.randint(1,3))

    
main()
