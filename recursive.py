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

def countdown(start,stop):
    if start < stop:
        print "blastoff!"
    else:
        print start
        countdown(start-1,stop)
def main():
    countdown(100,0)
main()

def adder(num,total):
    if num == "":
        return "The sum is " + str(total)
    else:
        total += float(num)
        num = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder (num, total)
def main():
    ans = adder (0,0)
    print ans
main()

def biggest (num):
    new = raw_input ("Next: ")
    if new == "":
		return num
    elif float(new) > float(num):
        return biggest (float(new))
    elif num > float(new):
        return biggest(num)

def main():
	ans = biggest (-float("inf"))
	print ans
main()

def smallest (num):
    new = raw_input ("Next: ")
    if new == "":
        return num
    elif float(new) < float(num):
        return smallest (float(new))
    elif float(num) < float(new):
        return smallest(float(num))

def main():
    ans = smallest (float("inf"))
    print ans
main()

def pow(x,n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)
def main ():
    ans = pow(10,3)
    print ans
    

main()
	
        
        





