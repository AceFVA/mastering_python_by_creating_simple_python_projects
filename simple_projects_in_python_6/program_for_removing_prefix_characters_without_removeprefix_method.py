# removeprefix() remove the characters at the beginning of the string that matches the function parameter.
# Create a program that do the same functionality without using removeprefix() function.

# set a variable with  a string of characters
string = "SB19 Ace SB19"

# set the prefix to be removed
prefix = "SB19"

# if string starts with prefix
if string.startswith(prefix):

# remove characters based on the desired prefix
    removed_prefix = string.replace(prefix, "", 1)

# print the string with removed prefix
print("Removed prefix: ", removed_prefix)


