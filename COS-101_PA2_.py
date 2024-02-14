#
# The first function would take a string and a number as parameters, 
# and it would print the string preceded by as many spaces as specified by the number. 
# Name the function as print_space.

# The second function would take a string as a parameter and print it on three lines, 
# with the string shifted to the right by a space on each consecutive line after the first line. 
# Name the function as cascade_three.


# Create a function that takes a string `string` and `Nspaces`
def print_space(string, Nspaces):
    
    # ouput a space multiplied by the given NSpaces input, and the given string
    print(' ' * Nspaces + string)

# Create a function that takes the string `string` and iterates through a range of 3 to run the print_space function
def cascade_three(string):
    
    # this will use i as the base start (1) and count up to 3
    # the i is then used as the NSpaces variable for number of spaces sent into the overload
    for i in range(3):
        print_space(string, i)

cascade_three('season')
