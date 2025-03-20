# Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# ask the user to input his/her full name in an incorrect casing
full_name = input("Enter your full name in an incorrect casing: ")

# convert casing into lower case
in_lower_case = full_name.lower()

# split input
input_list = in_lower_case.split()

# convert " " to "_"
in_snake_case = "_".join(input_list[:])

# print full name in snake case
print("Your full name in snake case: ", in_snake_case)
