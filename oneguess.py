import random
def guessing_1 (random1, guess , result):
    guess_1= """

The target was {}.
Your guess was {}.
That's under by {}.

""" . format (random1, guess, result)
    return guess_1

def guessing_2 (random1, guess , result):
    guess_2= """

The target was {}.
Your guess was {}.
That's over by {}.

""" . format (random1, guess, result)
    return guess_2
def guessing_3 (random1, guess):
    guess_3= """

The target was {}.
Your guess was {}.
That's correct!.

""" . format (random1, guess)
    return guess_3
def main ():
    minimum = int(raw_input ("What is the minimum number?: "))
    maximum = int (raw_input ("What is the maximum number?: "))
    random1 = random.randint (minimum, maximum)
    print "I'm thinking of a number between", str(minimum), "and", str(maximum)
    guess = int(raw_input ("What do you think it is?:"))
    result = abs(guess - random1)

   
    if random1>abs(guess):
        guess_1 = guessing_1(random1, guess, result)
        print guess_1
    elif random1 <abs(guess):
        guess_2 = guessing_2(random1, guess, result)
        print guess_2
    elif random1 ==abs(guess):
        guess_3 = guessing_3(random1, guess)
        print guess_3
main()


