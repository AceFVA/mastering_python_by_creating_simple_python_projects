# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format.
# Add zeros at the beginning to complete the 6 digit.

# ask the user to input any number starting from 0 to 1000
input_num = input("Enter a number between 0 and 1000: ")

# add zeros at the beginning to make it in a 6-digit format
with_zeros = input_num.zfill(6)

# print the digits
print(with_zeros)
