

def main ():
    minimum = raw_input ("What is the minimum number?: ")
    maximum = raw_input ("What is the maximum number?: ")
main()

def output (minimum, maximum):
    out= """
I'm thinking of a number from {} to {}.

""" .format (minimum, maximum)

def main ():
    youranswer= raw_input ("What do you think it is?:" )
main()
 
def output (target, guess, result):
    out= """


The target was {}.
Your guess was {}.
That's under by {}-{}={}

""" . format (target, guess, result)
    return out

