def countup(start, stop):
    if start > stop:
        print "blastoff!"
    else:
        print start
        countup(start+1, stop)

def main():
    countup(1,123)
main()

def countup(n):
    if n >= 100:
        print "blastoff!"
    else:
        print n
        countup (n+1)

def main():
    countup(0)
main()

def countdown(x):
    if x <= 0:
        print "blastoff!"
    else:
        print x
        countdown (x-1)
def main ():
    countdown(100)
main()




