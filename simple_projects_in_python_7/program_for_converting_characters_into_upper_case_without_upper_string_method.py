# upper() converts all characters of the string into upper case.
# Create a program that do the same functionality without using upper() function.

# set a variable with a string of characters
string = "AcE fRaNcIs V. aGuStIn"

# create an empty list of uppercased letters
upper_cased = []

# iterate all items in the given string
for char in range(len(string)):
# if char in string is in lower case,
    if string[char].islower():
# convert to upper case and add to the list
        swapped_case = string[char].swapcase()
        upper_cased.append(swapped_case)
# if char in string is not in lower case,
    else:
# add char to the list
        upper_cased.append(string[char])

# print the strinf in upper case
print("String in upper case: ", "".join(upper_cased))
