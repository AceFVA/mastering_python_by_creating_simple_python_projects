# center() add space characters at the beginning and at the end of the string to print the string at the center.
# Create a program that do the same functionality without using center() function.

# set a variable with string element
string = "Ace"

# set a variabel with the specified function parameter
length = 9

# find the number of remaining characters needed to fulfill the funciton parameter 
space_added = 9 - len(string)

# [space string] * (remaining space needed // 2) + string + [space string] * (remaining space needed // 2)
centered_string = (" " * (space_added // 2)) + string + (" " * (space_added // 2))

# print string at the center
# print string length for verification
print("String at the center: ", centered_string)
print("String length: ", len(centered_string))

