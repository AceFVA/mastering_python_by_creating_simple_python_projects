# ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using ljust() function.

# set a variable with string element
string = "Ace"

# set a variable with the desired string length
length = 9

# find the number of space to be added to fulfill the remaining characters
space_added = 9 - len(string)

# string + [space string] * remaining characters needed
with_spaces = string + (" " * space_added)

# print the string with spaces added and its length
print("String with spaces: ", with_spaces)
print("String length: ", len(with_spaces))
