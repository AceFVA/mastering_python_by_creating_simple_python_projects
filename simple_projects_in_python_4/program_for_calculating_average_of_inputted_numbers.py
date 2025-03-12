# Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the average.

# create an empty list as container for the numbers to be inputted
num_list = []

# set 2 variables with initialize value of 0 for summation and average
summation = 0
average = 0
 
# ask the user to input a number continuously until input is invalid
while True:
    input_num = int(input("Enter a number: "))
# add the number inputted on the list
    num_list.append(input_num)
# summation = summation + input_num
    summation += input_num
# average = summation / number of all items on the list
    average = summation / len(num_list)

# print average
    print("The total average is: ", average)
