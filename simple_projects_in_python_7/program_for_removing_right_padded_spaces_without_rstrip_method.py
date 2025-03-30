# rstrip() remove the space characters at the end of the string.
# Create a program that do the same functionality without using rstrip() function.

# set a variable with a string element
string = "      Ace      "

# use negative indexing to indice string
# use lstrip()
removed_rspaces = string[::-1].lstrip()

# print the string without the right-padded spaces
print("String without right-padded spaces: ", removed_rspaces[::-1])
