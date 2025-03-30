# removesuffix() remove the characters at the end of the string that matches the function parameter.
# Create a program that do the same functionality without using removesuffix() function.

# set a variable with a string element
string = "SB19 Ace SB19"

# set the suffix to be removed
suffix = "SB19"

# if the string ends with the given suffix
if string.endswith(suffix):
# replace the characters with "" based on thr given suffix
    removed_suffix = string[::-1].replace(suffix[::-1], "", 1)
# print the string without the suffix
print(removed_suffix[::-1])
