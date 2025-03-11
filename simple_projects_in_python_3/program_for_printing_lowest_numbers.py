# Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the lowest number

# create a variable with an empty list
num_list = []

# ask the user to input an inital number
num = int(input("Enter an inital number: "))
print ("The lowest number is: ", num)

# insert the initial number to the list
num_list.insert(0, num)

# ask the user to input a number continuously until input is invalid
# if num is less than the number from the list at index 0,
# print num as the lowest number
# insert num to the list at index 0
# if the number from the list at index 0 is less than num,
# print the number 
# insert num to the list at index 1
