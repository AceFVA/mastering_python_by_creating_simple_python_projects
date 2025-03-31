# rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using rjust() function.

# set a variable with string element
string = "Ace"

# set a variable for the specified function parameter
parameter = 9

# identify the number of spaces to be added to satisfy the given parameter
space_added = 9 - len(string)

# add space to the beginning of the string
with_space = " " * space_added + string

# print the string with the beginning spaces
print("String with beginning spaces: ", with_space)
