# zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using zfill() function.

# set a variable with string of characters
string = "Ace"

# set a variable with the specified parameter
parameter = 9

# identify the number of zeros to be added to fulfill the parameter given
zeros_added = parameter - len(string)

# add zeros at the beginning of the string
with_zeros = "0" * zeros_added + string

# print the string with the zeros added
print("String with zeros: ", with_zeros)

