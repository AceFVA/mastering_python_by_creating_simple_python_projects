# Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number from highest to lowest. Clue: sort() function

# create an empty list as container for the numbers to be inputted
num_list = []

# ask the user to input a number continuously until input is invalid
while True:
    input_num = int(input("Enter a number: "))
# add the number inputted on the list
    num_list.append(input_num)
# sort the numbers in descending order
    num_list.sort(reverse = True)

# print the numbers
    print("Your numbers in descending order: ", *num_list, sep=" ")
