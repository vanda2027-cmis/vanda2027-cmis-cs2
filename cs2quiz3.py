#Section 1: Terminology
# 1) What is a recursive function?
# It is when the function repeats by calling itself 
#
#
# 2) What happens if there is no base case defined in a recursive function?
# The function will repeat itself until it gets to the limit of where the computer will stop 
#
#
# 3) What is the first thing to consider when designing a recursive function?
# The base case and the recursive case
#
#
# 4) How do we put data into a function call?
# By setting a value to a variable
#
# 
# 5) How do we get data out of a function call?
# by printing and returning values.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8 
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 0
#b3 = 3

#c1 = 1
#c2 = 4
#c3 = 19

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def number(total):
#start of base case
	given = raw_input("Next Number: ")
	if total == "":
		return "The average is {}".format(total)
        #end base case
        #start recursive case
    elif given == 0:
        amoutofnumbers += 1
        total += given
    else:
        total == (total + float(given )) / amountofnumbers
number(total)
        #end recursive case



def main():

   
    main()


        
