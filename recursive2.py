def countdown(start,stop):
    if start < stop:
        print "blastoff!"
    else:
        print start
        countdown(start-1,stop)
def main():
    countdown(100,0)
main()



 

