# index() return the first location of the function parameter in the string.
# Create a program that do the same functionality without using index() function.

# set a variable with the string element
string = "Ace Francis V. Agustin"

# set a variable with the given parameter
parameter = "a"

# find parameter in the given string
first_location = string.find(parameter)

# if output is not equal to -1:
if first_location != -1:
# print the first location of the parameter
    print("First Location: ", first_location)

# if output is -1
else:
# print ValueError
    print("ValueError")
