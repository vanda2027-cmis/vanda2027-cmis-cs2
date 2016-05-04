import random
def game(guess, radom)
    random = random.randint(1,100)
    guess = int(raw_input("Guess a number: "))
    
    if random == guess:
        print "That's correct!"
    elif random > guess
        print "That's too high"
    elif random < guess
        print "That's too low"

