#Section 1: Terminology
# 1) What is a recursive function?
# It is when the function repeats by calling itself 
# 1 point
#
# 2) What happens if there is no base case defined in a recursive function?
# The function will repeat itself until it gets to the limit of where the computer will stop 
# 1 point 
#
# 3) What is the first thing to consider when designing a recursive function?
# The base case and the recursive case
# 1 point
#
# 4) How do we put data into a function call?
# By setting a value to a variable
# 1 point
# 
# 5) How do we get data out of a function call?
# by printing and returning values.
# 1 point
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8   1 point
#a2 = 8   1 point
#a3 = -1  1 point

#b1 = 2   1 point
#b2 = 2   1 point
#b3 = 4   1 point

#c1 = 1   0 point
#c2 = 4   1 point
#c3 = 45  1 point

#d1 = 6   1 point
#d2 = 8   1 point
#d3 = 4   1 point

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def number(total):
#start of base case +2 base case
	given = raw_input("Next Number: ")
	if total == "":
		return "The average is {}".format(total)
        #end base case
        #start recursive case +2 recursion case
    elif given == 0:
        amoutofnumbers += 1
        total += given
    else:
        total == (total + float(given )) / amountofnumbers
number(total)
        #end recursive case



def main():
        outcome = number #+1 main

   
    main()


        
