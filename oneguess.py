
def main ():
    minimum = raw_input ("What is the minimum number?: ")
    maximum = raw_input ("What is the maximum number?: ")
   
    if target> str(abs(guess)):
        guess_1 = guessing_1(target, guess, result)
    print guess_1
    elif target < str(abs(guess)):
        guess_2 = guessing_2(target, guess, result)
    print guess_2
    elif target == str(abs(guess)):
        guess_3 = guessing_3(target, guess, result)
    print guess_3
main()


def guessing_1 (target, guess , result):
    guess_1= """

The target was {}.
Your guess was {}.
That's under by {}.

""" . format (target, guess, result)

def guessing_2 (target, guess , result):
    guess_2= """

The target was {}.
Your guess was {}.
That's under by {}.

""" . format (target, guess, result)
def guessing_3 (target, guess , result):
    guess_3= """

The target was {}.
Your guess was {}.
That's under by {}.

""" . format (target, guess, result)


