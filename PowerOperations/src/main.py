#!/usr/bin/python

"""
Basic power/root calcuation program to demonstrate:

* functions
* arguments
  * defaults
* parameters

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

# Necessary imports
import math
import suffix

# Write function to calculate result of various numbers 
#       raised to various powers.
def raise_to_power(number, power):
  """ Calculates result of a number raised to a power """
  sq_root = math.pow(number, power)
  return sq_root

# TODO: Write function to calculates nth root of a number 
#       by raising to fractional power

# Print program introduction
print("Power and root calculator", end = "\n\n")

# Collect user information
user_num = int(input("Enter a number: "))
user_pow = int(input("Enter a power: "))

# Perform calculations using functions
raised = raise_to_power(user_num, user_pow)

# Use suffix to get the proper number suffix: 1st, 2nd...
num_suffix = suffix.determine(user_pow)

# Print results for both computations using same power
print(f"{user_num} raised to the {user_pow}{num_suffix} power: {raised}")
print(f"{user_num} taken to the {user_pow}{num_suffix} root: {rooted}")
