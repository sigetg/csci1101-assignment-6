# Write a program that prints out a hollow square, with the edges made of
# asterisks (*s).  Specifically, you must create a function named print_square()
# that takes the square's side length as the single parameter.  Your top-level
# program must prompt the user for the side length, which must be positive.
# You can assume the value entered is an integer.  Then call your print_square()
# function to print the square with the appropriate side lengths.  For example,
# print_square(4) should print the following:
#
# ****
# *  *
# *  *
# ****
#
# There are several ways to approach the print_square() function.  If you aren't
# sure where to start, consider following these steps:

# First, only print a single row of *s of the appropriate length.
# Then, extend that to print out a filled in square that has *s in the middle of
#     the square also.  Something like this for print_square(4):
#
# ****
# ****
# ****
# ****
#
# Finally, modify the function to print spaces (" ") instead of *s in the
#     interior of the square.
#
# Note that if you want to print a string without the automatic new line added,
# you can pass print() a second argument of end="" to tell it not to print
# anything at the end of your string. For example:
#
# print("*",end="")
#
# That will print the * but not print the new line afterwards.  This allows you
# to print multiple strings to the same line of output.
#
# Again, you must print the square out in your print_square() function.
#
# Your input and output messages must conform to the following examples:
#
# Enter side length: 0
# side length must be positive!
#
# Enter side length: 4
# ****
# *  *
# *  *
# ****
#
# Enter side length: 2
# **
# **
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import sys

def print_square(x):
    y = x + 1
    z = 1
    while z<=x:
        if z == 1 or z == x:
            print("*"*x)
        else:
            print("*"," "*(x - 2),"*",sep="")
        z+=1
        

side_length = int(input("Enter side length: "))
if side_length <= 0:
    print("side length must be positive!")
    sys.exit

print_square(side_length)



















