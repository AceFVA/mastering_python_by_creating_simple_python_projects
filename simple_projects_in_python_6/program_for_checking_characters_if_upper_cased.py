# isupper() check if all characters of the string is on upper case.
# Create a program that do the same functionality without using isupper() function.


# create a variable with string type element
string =  "ACE FRAnCIS V. AGUSTIN"

# create a variable the numbers of uppercased and  non-alphanumeric characters
uppercased = 0

# iterate all characters in the given string

# if a character is not in lowercase,

# uppercase variable + 1

# if a character is not alphanumeric,

# uppercase variable + 1

# if uppercase variable is equal to the length of the string,
if uppercased == len(string):
# print "All characters are in UPPERCASE"
    print("All characters are in UPPERCASE")
# if uppercase variable is not equal to the length of the string
else:
# print "Not all characters are in UPPERCASE"
    print("Not all characters are in UPPERCASE")
