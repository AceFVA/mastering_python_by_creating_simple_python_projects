# isupper() check if all characters of the string is on upper case.
# Create a program that do the same functionality without using isupper() function.


# create a variable with string type element
string =  "ACE FRANCIS V. AGUSTIN"

# create a variable the numbers of uppercased and  non-alphanumeric characters
uppercased = 0

# iterate all characters in the given string
for char in string:
# if a character is not in lowercase,
    if not(char.islower()):
# uppercase variable + 1
        uppercased += 1
# if a character is not alphanumeric,
    elif not(char.isalnum()):
# uppercase variable + 1
        uppercased += 1

# if uppercase variable is equal to the length of the string,
if uppercased == len(string):
# print "All characters are in UPPERCASE"
    print("All characters are in UPPERCASE")
# if uppercase variable is not equal to the length of the string
else:
# print "Not all characters are in UPPERCASE"
    print("Not all characters are in UPPERCASE")
