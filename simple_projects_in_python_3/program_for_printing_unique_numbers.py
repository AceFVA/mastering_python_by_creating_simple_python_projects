# Create a program that ask user to input 10 numbers.
# Display all numbers. For numbers with duplicate, display only the first entry.

# ask the user to input 10 numbers with spaces in between
numbers = input("Input 10 numbers separated by space: ")    # example "1 2 3 4 5 6 7 1 2 3"

# create a list for the numbers given by the user
num_list = numbers.split()

# set a variable with an empy list as a container for unique numbers
unique_num = []

# iterate an item in range(10) using for loop
# if number not in the unique list, 
# add number to that list
# print the number

#experiment

for i in range(10):
    if num_list[i] not in unique_num:
        unique_num.append(num_list[i])
        print(unique_num[i])
