# count() return how many time the function parameter appear in the string.
# Create a program that do the same functionality without using count() function.

# set a variable with string of characters
string = "MAHALIMA"

# set a variable for the specified function parameter
parameter = "A"

# set a variable with an initial value of 0 for repetition counts
parameter_count = 0

# iterate all characters in the given string
for char in string:
# if char is equal to the function parameter,
    if char == parameter:
# add char to the list
        parameter_count += 1

# print the count of function parameter that is in the string
print("Parameter count: ", parameter_count)
