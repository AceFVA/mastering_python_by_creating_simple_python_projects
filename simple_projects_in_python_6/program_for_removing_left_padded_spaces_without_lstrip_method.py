# lstrip() remove the space characters at the beginning of the string.
# Create a program that do the same functionality without using lstrip() function.

# set a variable with a string of characters
string = "      Ace      "

# use negative indexing to indice string
# use rstrip()
removed_lspaces = string[::-1].rstrip()

# print the string without the right-padded spaces
print("String without left-padded spaces: ", removed_lspaces[::-1])
