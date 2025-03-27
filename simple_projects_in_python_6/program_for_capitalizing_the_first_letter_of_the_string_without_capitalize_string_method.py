# capitalize() makes the first letter of the string, capital letter. And all other letter in small case.
# Create a program that do the same functionality without using capitalize() function.

# set a variable with a string element
string = ".!? ace francis v. agustin"

# iterate all characters in the given string
for char in string:
# check if the iterated character is a letter
    if char.isalpha():
# replace the first alphabet character by its capitilized case
        capitalized_string = string.replace(char, char.upper(), 1)
# end loop if the first letter was capitalized
        break

# print string in capitalized case
print(capitalized_string)
