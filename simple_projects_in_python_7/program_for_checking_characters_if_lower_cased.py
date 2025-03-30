# islower() check if all characters of the string is on lower case.
# Create a program that do the same functionality without using islower() function.

# set a variable with a string of characters
string = "ace francis v. agustin"

# set a variable with an initialized value of 0 for counting number of lowercased and alphanumeric characters
lowercased = 0

# iterate all items in the given string
for char in string:
# if char is not in uppercase,
    if not(char.isupper()):
# lower case variable += 1
        lowercased += 1
# if char is in alphanumeric character,
    elif not(char.isalnum()):
# lower case variable += 1
        lowercased += 1

# if the length of lower case variable equal to length of the string
if lowercased == len(string):
# print True
    print("True")

# if the length of lower case variable not equal to length of the string,
else:
# print False
    print("False")
