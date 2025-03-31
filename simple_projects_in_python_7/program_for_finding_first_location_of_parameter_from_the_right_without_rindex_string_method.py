# rindex() return the first location of the function parameter in the string starting from the last character.
# Create a program that do the same functionality without using rindex() function.

# set a variable with a string od characters
string = "Ace Francis V. Agustin"

# set a variable for the function parameter
parameter = "A"

# find if there is a parameter present in the string
locaiton = string.find(parameter)

# create a dictionary for the location of every parameter found
locations = {}

# iterate all characters in the string
# if character is equal to parameter,
# add the char in the dictionary
# if location is not equal to -1,
if location != -1:
# print the location of the parameter startinb from the right
    print(max(locations.values()))
# if location is equal to -1,
else:
# print ValueError
    print("ValueError")
