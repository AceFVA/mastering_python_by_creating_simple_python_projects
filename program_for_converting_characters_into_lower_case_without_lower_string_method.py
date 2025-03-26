# lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# set a variable with an element of string of characters
string = "AcE fRaNcIs V. aGuStIn"

# create an empty list for lower cased characters
lower_cased = []

# create a for loop to iterate all items in the given string
for char in range(len(string)):
# if char in string is in upper case,
    if string[char].isupper():
# change the case of the char and add to the list
        swapped_case = string[char].swapcase()
        lower_cased.append(swapped_case)
# if char is not in upper case,
    else:
# add char to the list
        lower_cased.append(string[char])

# print the string of characters in lower case
print("".join(lower_cased))
