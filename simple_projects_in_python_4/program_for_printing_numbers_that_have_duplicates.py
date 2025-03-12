# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# ask the user to input 10 numbers with spaces in between
numbers = input("Enter 10 numbers with spaces in between: ")    # example "1 2 3 4 2 3 4 5 8 9"

# create a list for the numbers inputted
num_list = numbers.split()
# create an empty list
with_duplicate = []

# create a for loop to iterate an item from the list
for i in range(10):
# verify if a number have duplicate
    if num_list.count(num_list[i]) >= 2:
# add the number on the empty list if with duplicate
# if a number is already on the list, remove the number
        if num_list[i] in with_duplicate:
            with_duplicate.remove(num_list[i])
        with_duplicate.append(num_list[i])
# sort the number in ascending order
with_duplicate.sort()
# print the numbers with duplicate
print("The numbers with duplicate are:", " ".join(with_duplicate))
