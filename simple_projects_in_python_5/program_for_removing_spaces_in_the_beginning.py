#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning.
#Print the input without the spaces in the beginning.

# ask the user to enter his/her fullname with several space characters at the beginning.
full_name = input("Please enter your full name with spaces at the beginning: ")
# remove left padded spaces
# print full name
print(full_name.lstrip())
