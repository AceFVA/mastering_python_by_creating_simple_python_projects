# endswith() check if the string end part matches the function parameter.
# Create a program that do the same functionality without using endswith() function.

# create a variable with string of characters
string = "Ace Francis V. Agustin"
# create the function parameter
end_part = "Agustin"

# if the end part of the given string is equal to the function parameter,
if string[-1:-(len(end_part)+1):-1] == end_part[::-1]:
# print True
    print("True")
# if the end part of the given string is not equal to the function parameter
else:
# print False
    print("False")
