#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 9 <= 89
#b) 3*4 != 4*7
#c) 4 == 6
#
#2) What does 'return' do?
# It spits out a value.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) It tells the begining and the end of function definition.
#b) It gives a value to a true statement.
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) sqrt 3
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) True
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5 
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)



#Giving the raw input to type numbers in
def main ():
    print "Type in 3 different numbers (decimals are OK!)"
    float(raw_input("A:"))
    float(raw_input("B:"))
    float(raw_input("C:"))
    
  

#to find the largest number        
def numbers (a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>b and c>a:
        return c
    else:
        return False

x = numbers(a,b,c)
def output (x):
    if x == False:
        return "You didn't follow directions."
    else:
        return "The largest number was {}.". format (x)



 
