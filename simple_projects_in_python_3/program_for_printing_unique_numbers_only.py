# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# ask the user to input 10 numbers
numbers = input("Enter 10 numbers with spaces  in between: ")    #example "1 1 2 3 4 5 6 7 8 8"

# create a list for the numbers given by the user
num_list = numbers.split()

# set a variable with an empy list
unique_num = []

# iterate an item in range(10)
for i in range(10):
# if the count of a number is less than 2,
    if num_list.count(num_list[i]) < 2:
# add the number to that list
        unique_num.append(num_list[i])
        
# print the unique numbers
print("The unique numbers are:", " ".join(unique_num))
