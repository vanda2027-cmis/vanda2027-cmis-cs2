import random



def rounds(numrounds, correct):
    if numrounds == 0:
        out = """You got {} rounds correct.""".format(correct)
        print out
    else:
        out = """Starting round {}.""".format(numrounds)
        print out

        correct += game(random.randint(1,100),5)
        return rounds(numrounds - 1, correct)

def game(guess, tries):
    guess = raw_input("Guess a number: ")
    randomnum = (random.randint(1,100))
    if randomnum == int(guess):
        print "That's correct!"
    elif tries == int(1):
        print "You lose"
        return 0
    elif randomnum < int(guess):
        print "That's too high"
        return game(randomnum, tries - 1)
    elif randomnum > int(guess):
        print "That's too low"
        return game(randomnum, tries - 1)

def main():
    print rounds(5,0)
  
    
main()

