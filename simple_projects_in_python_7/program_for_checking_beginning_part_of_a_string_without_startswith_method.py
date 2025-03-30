# startswith() check if the string beginning part matches the function parameter.
# Create a program that do the same functionality without using startswith() function.

# set a variable with a string of characters
string = "Ace Francis V. Agustin"

# set a parameter
beginning_part = "Ace"

# if the string begins with the given parameter
if string[:len(beginning_part)] == beginning_part:
# print True
    print("True")
# if the string does not begins with the given parameter,
else:
# print False
    print("False")
