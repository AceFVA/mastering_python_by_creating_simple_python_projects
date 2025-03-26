# lstrip() remove the space characters at the beginning of the string.
# Create a program that do the same functionality without using lstrip() function.

# input any characters with left padded spaces
input_str = input("Enter any characters with left-padded spaces: ")

# initialize a variable at value of 0 as container for left-padded spaces
left_spaces = 0

# create a for loop that identifies the left-padded spaces
for i in range(len(input_str)):
    if input_str[i] == " ":
        left_spaces += 1
    else:
        break

# print the input without left-padded spaces
print("Removed left-padded spaces: ", input_str[left_spaces:])
