# swapcase() reverse the casing of each of the character of the string.
# Create a program that do the same functionality without using swapcase() function.

# set a variable with string element
string = "AcE fRaNcIs V. aGuStIn"

# set a variabel with an empty string element
swapped_string = ""

# iterate all characters in the given string
for char in range(len(string)):
# if character is in uppercase,
    if string[char].isupper():
# swapped string variable += character in lowercase
        swapped_string += string[char].lower()
# if character is not alnum,
    elif not(string[char].isalnum()):
# swapped string variable += character
        swapped_string += string[char]
# if character is in lowercase,
    else:
# swapped string variable += character in uppercase
        swapped_string += string[char].upper()

# print string in swapped case
print("String in swapped cases: ", swapped_string)
