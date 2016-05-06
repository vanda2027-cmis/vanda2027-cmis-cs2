import random
def rounds(numrounds, correct):
    if numrounds == 0:
        return "You got " + str(correct) + "rounds correct."
    else:
        return "Starting round: " + str(numrounds)
    
def game(guess, tries):
    random = (random.randint(1,100))
    put = int(raw_input("Guess a number: "))
    if random == guess:
        print "That's correct!"
        return game(guess, tries - 1)
    elif random > guess:
        print "That's too high"
        return game(guess, tries - 1)
    elif random < guess:
        print "That's too low"
        return game(guess, tries - 1)

def main():
    res = rounds(3, 0)
    print res
    game(guess, tries)
    
    
main()

