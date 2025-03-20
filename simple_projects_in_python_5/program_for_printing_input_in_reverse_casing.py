# Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# ask the user to input his/her full name
full_name = input("Enter your full name: ")

# swap the casing to its reversed casing
reversed_casing = full_name.swapcase()

# print full name in reversed casing
print("Your full name in reversed casing: ", reversed_casing)

