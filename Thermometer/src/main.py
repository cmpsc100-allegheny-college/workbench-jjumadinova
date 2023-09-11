#!/usr/bin/python

"""
Temperature conversion program used to demonstrate:

* interactive programs
* data types
* basic computation

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

def main():
    
    # Print program name
    print("Farenheight to celsius converter", end = "\n\n")

    # Request user input
    temp_f = input("Enter the temperature (without units): ")
    print(temp_f)

    # Perform calculation
    temp_c = int(temp_f) - 32
    temp_c *= 5/9

    # Report result
    print("The temperature in Celsius is: ", temp_c)

if __name__ == "__main__":
    main()
