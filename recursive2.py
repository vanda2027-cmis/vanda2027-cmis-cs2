def countdown(start,stop):
    if start < stop:
        print "blastoff!"
    else:
        print start
        countdown(start-1,stop)
def main():
    countdown(100,0)
main()

#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def number(total = 0):
#start of base case
	given = raw_input("Next Number: ")
	if given != "":
		print "The average is {}".format(total)
#end of base case
#start of recursive case
	elif given % 2 == 0:
		given = 0
		amount += 0
		number(total)
	else:
		amount += 1
		total = (total + float(given)) / amount
		number(total)
		

number()


#def adder2(running_total = 0):
#	print "The running total is {}.".format(running_total)
#	number = raw_input("Next Number: ")
#	if number != "":
#		running_total += float(number)
#		adder2(running_total) 
#	else:
#		print "The sum is {}.".format(running_total)
#adder2()



 

