# Create a program that ask the user to input their fullname with several space characters at the beginning.
# Print the input without the spaces in the beginning.

# ask the user to enter his/her fullname with several space characters at the beginning.
full_name = input("Please enter your full name with spaces at the beginning: ")

# remove left padded spaces
removed_spaces = full_name.lstrip()

# print full name
print("Your full name is: ", removed_spaces)
