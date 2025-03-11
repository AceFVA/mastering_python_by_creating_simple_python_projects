# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# ask the user to input 10 numbers with spaces in between
numbers = input("Enter 10 numbers with spaces in between: ")
# example: "100 9 8 7 6 5 4 3 2 1"

# create a list of numbers entered by the user
num_list = numbers.split()

# set a variable as a container for the first number
first_num = num_list[0]

# create a for loop and iterate all items from the list except for the first number
for i in range(1,10):
# difference = first number - second-last number
    first_num = int(first_num) - int(num_list[i])
# print the difference
print(first_num)
