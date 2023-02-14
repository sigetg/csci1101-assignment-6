# Write a program to compute the square root of a number.  You are NOT ALLOWED
# to use any built-in math functions for this problem including abs() and all
# math module functions (you can't use math.sqrt(), math.pow(), math.fabs(),
# etc).  You will instead be using the Babylonian method (also called Heron's
# method) to approximate the square root via repeated calculations that are
# guaranteed to converge to the actual square root value.
#
# The Babylonian method requires three inputs to calculate the square root of x:
#
# x: the value to take the square root of
# tolerance: the maximum allowed error in the calculation
# guess: an initial guess for what the square root will be
#
# The procedure relies on using the current estimate of the square root to
# calculate a better estimate of the square root.  The procedure guarantees that
# each subsequent estimate will be closer to the "true" square root than the
# last.  You can read about why that's the case in the article above.
# Specifically, each better estimate is the mean of the current estimate and
# (x / current estimate):
#
#                        x
#          current + ---------
#                     current
# better = -------------------
#                  2
#
# Procedures like this require a stopping condition, otherwise you could
# continue computing better estimates from the previous estimates forever.  The
# Babylonian method uses the provided tolerance to determine when to stop and
# return the best estimate computed.  A common misconception is that you use the
# tolerance as an error from the "true" square root.  That is not the case here
# - the entire point of this method is to compute the square root assuming we
# don't already know it.  Instead, because each estimate is guaranteed to be
# closer to the "true" square root than the last, we can compare the difference
# in the new better estimate and the previous estimate that was used to get that
# estimate.  The difference between the two estimates might be positive or
# negative depending on which one is larger, so you have to take the absolute
# value of the difference.  If that difference is less than the provided
# tolerance then the procedure ends and the best estimate computed is returned.
#
# Here is an example of the procedure to help illustrate how it works.  In this
# example, we are taking the square root of 16, with an error tolerance of 1,
# and an initial guess of 16:

# 1) The first iteration computes a better estimate of (16 + 16/16)/2 = 8.5.
# 2) The absolute value of the difference between this estimate and the last
#    estimate is |8.5 - 16| = 7.5.
# 3) 7.5 is greater than the tolerance of 1, so we continue looking for a better
#    estimate.
# 4) The second iteration computes a better estimate (8.5+16/8.5)/2 = 5.191.
# 5) The absolute value of the difference between this estimate and the last
#    estimate is |5.191 - 8.5| = 3.309.
# 6) 3.303 is greater than the tolerance of 1, so we continue looking for a
#    better estimate.
# 7) The third iteration computes a better estimate (5.191+16/5.191)/2 = 4.137.
# 8) The absolute value of the difference between this estimate and the last
#    estimate is |4.137 - 5.191| = 1.054.
# 9) 1.054 is greater than the tolerance of 1, so we continue looking for a
#    better estimate.
# 10) The fourth iteration computes a better estimate (4.137+16/4.137)/2 =
#     4.002.
# 11) The absolute value of the difference between this estimate and the last
#     estimate is |4.002 - 4.137| = 0.135.
# 12) 0.135 is less than the tolerance of 1, so we end the procedure and return
#     4.002 as the square root of 16.
#
# Note that the numbers above are rounded to 3 decimal places for printing only.
# The actual values used are stored to the maximum floating point accuracy
# throughout.
#
# You must create two functions.  First, you must create a function named
# absolute_value() that takes a single number as a parameter and returns the
# absolute value of that number.  Second, you must create a function named
# square_root() that takes two parameters: x (the value to take the square root
# of), and tolerance.  Both are floating points numbers. square_root() then uses
# x itself as the initial guess for the square root and uses the Babylonian
# method to return an estimate of the square root of x with relative tolerance
# given by the second parameter.  Note that your square_root() will have to call
# your own absolute_value() function as part of the procedure.
#
# Your top-level program must prompt the user for both x and the tolerance, then
# use your square_root() function to get the result.  Both x and the tolerance
# must be positive numbers.  Do not output anything in square_root() or
# absolute_value() functions (except when you are testing/debugging of course,
# which you'll need to take out before submission).  The result must be printed
# in the top-level program, to 10 decimal places of accuracy.
#
# Your input and output messages must conform to the following examples:
#
# Enter x: 0
# x must be positive!
#
# Enter x: 16
# Enter tolerance: 0
# tolerance must be positive!
#
# Enter x: 16
# Enter tolerance: 1
# Square root = 4.0022575248
#
# Enter x: 100
# Enter tolerance: 0.001
# Square root = 10.0000000001
#
# Note the order of outputs, capitalization of messages, spacing, etc.

import sys

def absolute_value(val):
    if val <= 0:
        return val * -1
    else:
        return val

def square_root(val, tol):
    guess = val
    difference = tol + 1
    while difference > tol:
        better = (guess + (x/guess)) / 2
        difference = absolute_value(better - guess)
        guess = better
    return guess

x = float(input("Enter x: "))
if x<=0:
    print("x must be positive!")
    sys.exit()

tolerance = float(input("Enter tolerance: "))
if tolerance<=0:
    print("tolerance must be positive!")
    sys.exit()

print(f"Square root = {square_root(x, tolerance):.10f}")






      


