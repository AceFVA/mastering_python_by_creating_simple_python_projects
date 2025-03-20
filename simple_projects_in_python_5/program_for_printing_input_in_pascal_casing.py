# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# ask the user to input his/her full name
full_name = input("Enter your full name: ")

# convert casing to title case
in_title_case = full_name.title()

# split the input by default
splitted_input = in_title_case.split()

# join each item to turn it into pascal case
pascal_case = " ".join(splitted_input)

# print full name in pascal casing
print("Your full name in pascal case: ", splitted_input)
